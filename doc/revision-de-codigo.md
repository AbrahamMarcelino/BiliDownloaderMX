# Revisión de código

Resultado de revisar el código de `src/` (versión 1.4.0, commit `104111c` del proyecto original). Todos los hallazgos se obtuvieron **leyendo el código**; ninguno se reprodujo ejecutando la aplicación, porque todavía no instala en Python 3.14 (ver el [plan de migración](plan-migracion-dependencias.md)).

- **Confirmado:** el error se deduce sin ambigüedad del código.
- **Probable:** depende del comportamiento de Qt o de la API y conviene comprobarlo al ejecutar.

Los problemas de compatibilidad con Linux y macOS ya están detallados en la [fase 5b del plan de migración](plan-migracion-dependencias.md#fase-5b--soporte-y-compilación-multiplataforma-linux-windows-y-macos) y aquí solo se resumen.

---

## 1. Errores

| # | Gravedad | Ubicación | Problema | Estado |
|---|---|---|---|---|
| 1 | Alta | `src/Lib/bd_client/__init__.py:8` | Importa `const.py`, que no está en el repositorio. Como `main.py` → `update.py` → `bd_client`, **la app no arranca** tras clonar el repositorio | Confirmado |
| 2 | Media | `src/main.py:50`, `:58` | `updateHighDpi()` (línea 50) lee la configuración **antes** de `update_cwd()` (línea 58). En Linux eso crea `data/userdata.json` en la carpeta desde la que se lanzó la app (no en `~/.bili_downloader`) y la opción «alta densidad (DPI)» se lee de ese archivo vacío, así que **se ignora**. En Windows (modo desarrollo) pasa lo mismo con `src/data/` | Confirmado |
| 3 | Media | `src/downloadthread.py:548-549, 565-566` | En macOS busca `ffmpeg.upx.exe` y usa `subprocess.CREATE_NO_WINDOW`, que no existe fuera de Windows (`AttributeError`): **no se puede combinar audio y video** | Confirmado |
| 4 | Media | `src/dialoglogin.py:52-55` | Al cerrar el diálogo de inicio de sesión, `dialog_finished` hace una espera activa (`while ...: pass`) en el hilo de la interfaz hasta que termine el hilo de consulta. Eso puede tardar 1,2 s más la petición en curso (hasta 15 s): **la ventana se congela** | Confirmado |
| 5 | Baja | `src/dialoglogin.py:46-55` | `load_finished` borra `self.load_thread` y llama a `close()`. Si eso emite `finished`, `dialog_finished` accede a `self.load_thread`, que ya no existe → `AttributeError` en la consola | Probable |
| 6 | Baja | `src/utils/configUtils.py:74` | `UserDataHelper.get()` usa `self.raw["key"]` (texto literal) en lugar de `self.raw[key]`: pedir `version` o `isnew` lanza `KeyError`. Hoy nadie lo llama así | Confirmado |
| 7 | Baja | `src/utils/configUtils.py:57`, `:113` | Borrar una clave que no existe (`set(clave, None)`) lanza `KeyError` (`pop` sin valor por defecto). Además, con `autosave=True` el borrado no se guarda | Confirmado |
| 8 | Baja | `src/Lib/bili_api/bangumi.py:108`, `:151` | Busca el mensaje de error con la clave numérica (`get["code"]`), pero en el JSON las claves son texto: siempre muestra «Error desconocido» | Confirmado |
| 9 | Baja | `src/Lib/bili_api/utils/wbisign.py:61-72` | Las claves WBI se guardan para siempre en una variable global. Bilibili las rota; si la app queda abierta mucho tiempo, las firmas pueden empezar a fallar hasta reiniciar | Probable |
| 10 | Baja | `src/Lib/bd_client/rconn_client/rconn.py:44-46` | `recv(4)` y `recv(json_len)` no se repiten en bucle; con una respuesta fragmentada el JSON llega incompleto. Solo afecta al actualizador (desactivado) | Confirmado |
| 11 | Baja | `src/Lib/bili_api/utils/loadImage.py:8-17` | Descarga portadas sin *timeout* (puede colgar el hilo), ignora la parte `?query` de la URL y no cierra la conexión | Confirmado |
| 12 | Baja | `src/selectionwidget.py:101`, `:114` | Compara el inicio del rango (base 1) con `select_max` (base 0): acepta rangos solapados en un elemento, como `1-3, 3-5`. Es inofensivo (solo marca dos veces la misma casilla) | Confirmado |
| 13 | Baja | `src/Lib/bili_api/utils/matchFomat.py:4`, `:7` | `[\d,a-zA-z]` admite comas y los caracteres entre `Z` y `a` (`[ \ ] ^ _` y el acento grave). Debería ser `[0-9a-zA-Z]` | Confirmado |
| 14 | Baja | `src/utils/version.py:7-8` | `check_version` falla (`IndexError`) si las versiones tienen distinto número de partes (`1.4` frente a `1.4.0`) | Confirmado |
| 15 | Mínima | `src/utils/removeSpecialChars.py:10` | Compara con la constante `_TITLE_SIZE_LIMIT` en lugar del parámetro `limit`; solo funciona porque siempre se pasa el valor por defecto o `None` | Confirmado |

## 2. Comportamientos a tener en cuenta

| Ubicación | Observación |
|---|---|
| `src/downloadwidget.py:207-209` | La opción que en el original se llama «最大下载线程数» (hilos de descarga) es en realidad el número de **descargas simultáneas** (en la interfaz traducida ya se llama así), y solo se lee al iniciar la app |
| `src/downloadwidget.py:392-414` | Al cerrar la app se borran los temporales de **todas** las tareas: las descargas en pausa no sobreviven a un reinicio |
| `src/downloadthread.py:563-564` | La salida de ffmpeg se descarta; si la combinación falla, no hay forma de saber por qué |
| `src/configwidget.py:210` | Las calidades disponibles se consultan con el **primer episodio** de la serie, no con el primero seleccionado |
| `src/dialoglogin.py:117-120` | Se guarda la caducidad de la sesión (`ts`), pero nunca se consulta; la validez solo se comprueba al arrancar con `nav` |
| `src/confirmwidget.py:220` | En series (MD), `meta["title"]` guarda el `season_id` en lugar del título. Hoy no afecta porque los nombres salen de `page_data` |
| `src/utils/configUtils.py` | `getUserData`/`setUserData` leen y reescriben todo el JSON en cada llamada, sin bloqueo entre hilos (lo usan tanto la interfaz como los `DownloadTask`) |
| `src/main.py:16-25`, `src/utils/open_folder.py`, `src/mainwindow.py:103` | Supuestos exclusivos de Windows o Linux; ver la [fase 5b del plan](plan-migracion-dependencias.md#5b1-ajustes-de-código-comunes) |

## 3. Seguridad

| Ubicación | Observación | Riesgo |
|---|---|---|
| `src/Lib/bili_api/utils/passport.py:13-37` | En Linux y macOS la clave que cifra la sesión se guarda en Base64 **junto** a los datos cifrados: es una ofuscación, no una protección real. Quien pueda leer `userdata.json` puede usar la sesión de Bilibili | Medio |
| `src/Lib/bili_api/utils/passport.py:31-32` | Cifrado AES en modo **ECB**. Con clave aleatoria por sesión y datos cortos el impacto es bajo, pero lo recomendable es un modo autenticado (GCM) | Bajo |
| `starter/main.c`, `build_nuitka_portable.bat` | El ejecutable pide **permisos de administrador** en cada arranque (`runas` y `--windows-uac-admin`). Según el código, lo necesita porque escribe `data/` y `Download/` dentro de la carpeta de instalación (p. ej. en `Program Files`) y para instalar la fuente en el sistema. Guardar los datos en la carpeta del usuario evitaría pedir estos permisos | Medio |
| `pickle` entre widgets | Solo se usa dentro del proceso con datos propios, así que no es explotable. Aun así, un `dict` normal o una `dataclass` evitaría el paso por bytes | Nulo |

## 4. Licencias

`src/Lib/xml2ass/__init__.py` no indica su origen. Sus funciones (`TestFreeRows`, `MarkCommentRow`, `WriteASSHead`, `ConvertFlashRotation`, `ReadCommentsBilibili`, `ProcessComments`…) coinciden con las de **[danmaku2ass](https://github.com/m13253/danmaku2ass)** de m13253, publicado bajo **GPLv3**, mientras que este proyecto es **MIT**. Conviene confirmar el origen del archivo y, si deriva de danmaku2ass, añadir el aviso de copyright y evaluar la compatibilidad de licencias (o sustituirlo por una implementación propia).

## 5. Calidad del código

- **Sin pruebas automatizadas.** Buenos candidatos para empezar, por ser funciones puras: `matchFomat`, `wbisign.sign_params`, `version.check_version`, `removeSpecialChars`, `sizefStr`, `cookieTools` y el análisis de rangos de `SelectionWidget`.
- **Código duplicado:**
  - `LaodInfoAV` y `LoadInfoBV` (y `LoadInfoMD` y `LoadInfoEP`) son casi idénticas.
  - El descifrado de la sesión se repite en `checkaccount.py`, `configwidget.py`, `downloadthread.py` y `settingswidget.py`.
  - La descompresión HTTP está copiada en `get_data` y `DataGetter`.
- **Código sin uso:**
  - Endpoints `pages`, `get_download_url`, `bangumi_url_v2`, `get_login_*_old`.
  - `bangumi.get_bangumi_url_v2()`, `cookieTools.get_cookie()` y `DownloadTask.t_stop()`.
- **Nombres con erratas:** `LaodInfoAV`, `matchFomat`, `SELECTTON_HELP`, `resault`, `Placeholde.png`.
- **Textos de la interfaz** escritos directamente en chino en el código y en los `.ui`, sin `tr()` ni archivos de traducción de Qt. Para traducir la interfaz al español habría que extraerlos (ver [siguientes pasos](#6-siguientes-pasos-sugeridos)).

## 6. Siguientes pasos sugeridos

1. Arreglar los errores 1 (`const.py`) y 2 (orden de `updateHighDpi`/`update_cwd`), que afectan al arranque.
2. Incluir los errores 3 y 4 en la fase 5b del plan de migración.
3. Aclarar la licencia de `xml2ass`.
4. Añadir pruebas unitarias para las funciones puras antes de migrar a PySide6 6.11.
5. Internacionalizar la interfaz con `QTranslator` (archivos `.ts`) para ofrecerla en español, que es el objetivo de esta adaptación.
