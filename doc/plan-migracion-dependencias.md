# Plan de trabajo: migración a bibliotecas actuales

> Objetivo: que BiliDownloader se ejecute y compile con **Python 3.14** y las **versiones actuales** de todas sus dependencias, sin fijar versiones antiguas.

Fecha de elaboración: 2026-09-22

---

## 1. Situación actual

El proyecto fija versiones pensadas para Python 3.10. En Python 3.14 **no se pueden instalar**: `pip install -r src/requirements.txt` falla porque PySide6 6.7.3 solo publica paquetes para Python < 3.13.

### Dependencias

| Biblioteca | Versión fijada | Versión actual (PyPI) | Uso en el código | Riesgo |
|---|---|---|---|---|
| PySide6 | 6.7.3 | 6.11.2 | Toda la interfaz (31 módulos), `pyside6-uic` / `pyside6-rcc` | **Alto** |
| Pillow | 9.5.0 | 12.3.0 | Indirecto: `qrcode.make()` → `save(format="PNG")` en `dialoglogin.py` | Bajo |
| qrcode | 8.2 | 8.2 | Generar el QR de inicio de sesión (`dialoglogin.py`) | Nulo |
| pycryptodome | 3.23.0 | 3.23.0 | AES en `Lib/bd_client`, `Lib/bili_api/utils/passport.py`; SHA256 en `compile_ui.py` | Nulo |
| brotli | 1.2.0 | 1.2.0 | Descompresión HTTP en `Lib/bili_api/utils/network.py` | Nulo |
| zstandard | 0.25.0 | 0.25.0 | Descompresión HTTP en `network.py` | Nulo (sustituible, ver fase 3) |
| pyperclip | 1.11.0 | 1.11.0 | Leer el portapapeles (`inputsetupwidget.py`) | Nulo |
| pywin32 (solo Windows) | 312 | última disponible | `win32crypt` para proteger la clave de la cookie (`passport.py`) | Bajo |
| Nuitka (compilación) | sin fijar | 4.2.2 | Scripts `build_nuitka_*.sh/.bat` | Medio |

**Conclusión:** el único bloqueo real es **PySide6**. Pillow cambia de versión mayor, pero el código no lo usa directamente. El resto ya está en su versión actual.

### Otros hallazgos

- `Lib/bd_client/const.py` no está en el repositorio (lo excluye `.gitignore`). Como `update.py` importa `BDClient`, **la app no arranca sin crear ese archivo** (ver `SETUP.md`, modo sin conexión).
- `src/update.py` ya tiene `NO_UPDATE = True`.
- El changelog 1.3.5 dice que se **volvió a Qt 6.7** porque en versiones posteriores las fuentes se veían borrosas cuando la adaptación a alta densidad (DPI) estaba desactivada. Es el principal riesgo de la migración.
- En Linux falta `patchelf`, que Nuitka necesita para compilar el ejecutable independiente.
- `build_nuitka_linux.sh` crea `~/.bili_downloader/` y copia ahí archivos. Hay que tenerlo en cuenta al probar.

---

## 2. Fases de trabajo

### Fase 0 — Preparación

- [ ] Crear una rama de trabajo (`migracion-dependencias`).
- [ ] Crear el entorno virtual con Python 3.14: `python3 -m venv venv` (el directorio `venv/` ya existe y está en `.gitignore`).
- [ ] Crear `src/Lib/bd_client/const.py` con `CONST_KEY = b""` para el modo sin conexión.
  - Nota: `SETUP.md` indica `CONST_KEY=""`, pero `hasher.update(_CONST_KEY)` requiere `bytes`. Verificarlo y, si aplica, corregir `SETUP.md`.
- [ ] Instalar `patchelf` en el sistema (`sudo dnf install patchelf`).

### Fase 1 — Actualizar `requirements`

- [ ] Quitar las versiones exactas (`==`) y usar mínimos compatibles (`>=`) en `src/requirements.txt`:
  ```text
  PySide6>=6.11
  qrcode[pil]>=8.2
  pycryptodome>=3.23
  brotli>=1.2
  zstandard>=0.25
  pyperclip>=1.11
  ```
  - `qrcode[pil]` declara Pillow como dependencia de qrcode, que es quien realmente lo usa. Así se elimina la entrada suelta `Pillow==9.5.0`.
- [ ] `src/requirements_win.txt`: `pywin32>=311` (o la última disponible).
- [ ] Instalar y confirmar que no hay conflictos: `pip install -r src/requirements.txt` y `pip check`.

### Fase 2 — PySide6 6.7 → 6.11 (fase principal)

- [ ] **Regenerar la UI**: borrar `src/.ui_compiled.cache` y los `ui_*.py` / `res_rc.py` generados, y ejecutar `python compile_ui.py` con el `pyside6-uic`/`pyside6-rcc` nuevos.
- [ ] Arrancar la app (`python src/main.py`) y corregir los errores de importación o de API que aparezcan.
- [ ] Revisar las señales declaradas con tipos en texto (`QtCore.Signal("quint64", "quint64")` en `update.py` y `downloadthread.py`). Siguen siendo válidas, pero hay que confirmar que no generan avisos.
- [ ] **Alta densidad (DPI)**: `main.py` desactiva el escalado con `QT_ENABLE_HIGHDPI_SCALING=0`. Probar con la opción activada y desactivada y comprobar que las fuentes no salen borrosas (el problema de la 1.3.5). Si vuelve a pasar, evaluar:
  - `QtGui.QGuiApplication.setHighDpiScaleFactorRoundingPolicy(...)` en lugar de desactivar el escalado.
  - Ajustar `HintingPreference` (hoy `PreferNoHinting`) o la estrategia de antialias.
- [ ] **Estilos Qt**: la lista de estilos sale de `QStyleFactory.keys()` y el elegido se guarda en la configuración. En Qt 6.7+ Windows incluye el estilo `windows11`. Comprobar que un estilo guardado que ya no exista no rompe el arranque (`QStyleFactory.create` devuelve `None`).
- [ ] Revisar en consola los avisos de obsolescencia (`DeprecationWarning`) de PySide6.

### Fase 3 — Resto de bibliotecas

- [ ] **Pillow 12**: probar el inicio de sesión por QR y comprobar que la imagen se genera y se muestra. No hay uso directo de `PIL` en el código.
- [ ] **pywin32** (Windows): probar que `win32crypt.CryptProtectData` / `CryptUnprotectData` siguen funcionando. Las cookies guardadas con la versión anterior deben poder leerse.
- [ ] **zstandard (opcional)**: Python 3.14 trae `compression.zstd` en la biblioteca estándar (PEP 784). Se puede sustituir `zstandard.decompress` en `network.py` (2 usos) y quitar la dependencia. Solo si se decide que el mínimo es Python 3.14.

### Fase 4 — Versión de Python

- [ ] Fijar el mínimo soportado: el que exija la versión elegida de PySide6 (consultar su `Requires-Python`), o **≥ 3.14** si se adopta `compression.zstd`.
- [ ] Actualizar `SETUP.md` (hoy dice "Python >= 3.10") y quitar las menciones a Python 3.8 si ya no aplican.
- [ ] Revisar con `python -W error::DeprecationWarning` que no se usa nada eliminado en 3.12–3.14.

### Fase 5 — Compilación con Nuitka 4.x

- [ ] Instalar Nuitka actual: `pip install -U nuitka`.
- [ ] Linux: ejecutar `src/build_nuitka_linux.sh` y confirmar que se genera `dist.nuitka.linux/BiliDownloader`.
- [ ] Windows: ejecutar `build_nuitka_portable.bat` y revisar que las opciones (`--windows-console-mode`, `--windows-uac-admin`, `--enable-plugins=pyside6`) siguen existiendo en Nuitka 4.
- [ ] Verificar que `nuitka_config/bili_api.nuitka-package.config.yaml` sigue incluyendo `Lib/bili_api/utils/data/*.json`.
- [ ] El lanzador en C (`starter/`) no depende de Python; solo recompilarlo si cambia la ruta del ejecutable.

### Fase 5b — Soporte y compilación multiplataforma (Linux, Windows y macOS)

Hoy el proyecto está pensado para Windows, con soporte parcial para Linux, y **no funciona en macOS**: varias comprobaciones son del tipo «si no es Linux, entonces es Windows». Esta fase deja la app funcionando en los tres sistemas y define cómo compilarla y distribuirla en cada uno.

> **Importante:** Nuitka **no compila de forma cruzada**. Cada ejecutable debe generarse en su propio sistema (Linux en Linux, Windows en Windows, macOS en macOS). Por eso se propone automatizarlo con GitHub Actions (5b.5).

#### 5b.1 Ajustes de código comunes

| Problema | Dónde | Afecta a | Solución propuesta |
|---|---|---|---|
| Se busca `ffmpeg.upx.exe` en cualquier sistema que no sea Linux | `downloadthread.py:549` | macOS | Usar `.upx.exe` solo si `sys.platform == "win32"`. Además, buscar primero el `ffmpeg` incluido y, si no existe, el del sistema con `shutil.which("ffmpeg")`; si no hay ninguno, mostrar un mensaje claro |
| `subprocess.CREATE_NO_WINDOW` se usa en cualquier sistema que no sea Linux; en macOS no existe y lanza `AttributeError` al combinar audio y video | `downloadthread.py:565` | macOS | Condicionar a `sys.platform == "win32"` |
| «Abrir carpeta» usa `os.startfile` (solo Windows); en Linux muestra «Esta función aún no está disponible en Linux» | `utils/open_folder.py` | Linux, macOS | `QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(path))`, que funciona en los tres |
| La carpeta de datos solo se define para Linux (`~/.bili_downloader`); en macOS se escribe en el directorio actual, que dentro de un `.app` puede ser `/` o de solo lectura | `main.py:update_cwd` | macOS | Usar `QtCore.QStandardPaths.writableLocation(AppDataLocation)` en los tres sistemas, migrando los datos de `~/.bili_downloader` si existen |
| `CHANGELOG.md`, `LICENSE` y `ffmpeg` se leen relativos a la carpeta de datos, por eso el script de Linux los copia a `$HOME` | `main.py`, `dialogchangelog.py` | Todos | Resolver los recursos de solo lectura respecto a la carpeta del ejecutable (o `Contents/Resources` en macOS) |
| `pyperclip` necesita `xclip`, `xsel` o `wl-clipboard` en Linux | `inputsetupwidget.py:39` | Linux | Sustituirlo por `QtGui.QGuiApplication.clipboard().text()` y **quitar la dependencia** |
| La fuente `HarmonyOS Sans SC` se instala en el sistema solo en Windows, y para eso la app pide permisos de administrador (`--windows-uac-admin`) | `main.py`, `utils/install_sysfont_windows.py` | Todos | Cargarla al iniciar con `QtGui.QFontDatabase.addApplicationFont(...)`, sin tocar el sistema. Así se puede **quitar la petición de administrador** en Windows |
| La clave que cifra la cookie solo se protege en Windows (`win32crypt`) | `Lib/bili_api/utils/passport.py` | Linux, macOS | *(Opcional)* Usar `keyring` (Llavero de macOS, Secret Service en Linux), con reserva al comportamiento actual |
| El actualizador abre el instalador con `cmd /c start` | `mainwindow.py:103` | Linux, macOS | Está desactivado (`NO_UPDATE = True`). Si se reactiva, limitarlo a Windows o hacerlo multiplataforma |

#### 5b.2 Linux

Problemas del `build_nuitka_linux.sh` actual:

- `mkdir $MAIN_DIR` falla si la carpeta ya existe (no usa `-p`).
- `cp -r ../ffmpeg` falla porque en Linux no existe esa carpeta.
- Mezcla **compilar** con **instalar** (escribe en `$HOME`).
- No ejecuta `compile_ui.py` ni se detiene ante errores.

Nuevo script propuesto (`src/build_linux.sh`):

```bash
#!/usr/bin/env bash
# Compila BiliDownloader para Linux con Nuitka
set -euo pipefail
cd "$(dirname "$0")"

python compile_ui.py

python -m nuitka \
  --standalone \
  --enable-plugins=pyside6 \
  --user-package-configuration-file=nuitka_config/bili_api.nuitka-package.config.yaml \
  --include-data-files=../CHANGELOG.md=CHANGELOG.md \
  --include-data-files=../LICENSE=LICENSE \
  --include-data-dir=font=font \
  --linux-icon=res/icon/icon.png \
  --output-dir=../dist/linux \
  --output-filename=BiliDownloader \
  --deployment \
  main.py
```

- **Distribución recomendada: AppImage**. Se genera a partir de la carpeta *standalone*, un archivo `.desktop` y el icono, con `appimagetool`. Funciona en la mayoría de distribuciones sin instalar nada.
- **Dependencias del sistema:** `patchelf` para compilar; `ffmpeg` para usar la app (`sudo dnf install patchelf ffmpeg-free` en Fedora, `sudo apt install patchelf ffmpeg` en Debian/Ubuntu). La combinación usa `-c copy`, así que basta con `ffmpeg-free`.
- Para máxima compatibilidad, compilar en una distribución con glibc antigua (p. ej. en un contenedor con Ubuntu LTS anterior).
- Comprobar que se incluyen los complementos de Qt para **Wayland** además de X11.

```ini
[Desktop Entry]
Type=Application
Name=BiliDownloader
Comment=Descargador de videos de Bilibili
Exec=BiliDownloader
Icon=bilidownloader
Categories=Network;AudioVideo;
Terminal=false
```

#### 5b.3 Windows

Ya existen `build_nuitka_portable.bat` y `build_nuitka_test.bat`. Cambios:

- Añadir `python compile_ui.py` al inicio y parar si falla.
- Incluir `CHANGELOG.md`, `LICENSE`, `font/` y `ffmpeg/ffmpeg.upx.exe` con `--include-data-files` / `--include-data-dir`.
- Quitar `--windows-uac-admin` una vez que la fuente se cargue con `addApplicationFont` (5b.1).
- Quitar `--jobs=16` fijo (Nuitka usa por defecto los núcleos disponibles).
- `ffmpeg`: hoy se descarga a mano desde un enlace de Lanzou con contraseña (ver `SETUP.md`). Sustituirlo por una compilación oficial con licencia clara (p. ej. las de gyan.dev o BtbN, que ya incluyen AV1).
- **Distribución:** carpeta portable en `.zip` y, opcionalmente, un instalador con **Inno Setup** (el instalador original no está en el repositorio).
- El lanzador en C (`starter/`) es solo para Windows y compila con `tcc`; se mantiene igual.

#### 5b.4 macOS

- Nuevo script `src/build_macos.sh`:

  ```bash
  #!/usr/bin/env bash
  # Compila BiliDownloader.app para macOS con Nuitka
  set -euo pipefail
  cd "$(dirname "$0")"

  python compile_ui.py

  python -m nuitka \
    --standalone \
    --macos-create-app-bundle \
    --macos-app-name=BiliDownloader \
    --macos-app-icon=res/icon/icon.icns \
    --enable-plugins=pyside6 \
    --user-package-configuration-file=nuitka_config/bili_api.nuitka-package.config.yaml \
    --include-data-files=../CHANGELOG.md=CHANGELOG.md \
    --include-data-files=../LICENSE=LICENSE \
    --include-data-dir=font=font \
    --output-dir=../dist/macos \
    --deployment \
    main.py
  ```

- **Icono:** generar `res/icon/icon.icns` a partir de `icon.png` (`iconutil` o `sips`).
- **Arquitecturas:** compilar por separado en Apple Silicon (`arm64`) y en Intel (`x86_64`), o solo `arm64` si se decide no dar soporte a Intel.
- **ffmpeg:** incluir un binario estático para cada arquitectura dentro del `.app`, o usar el de Homebrew (`brew install ffmpeg`) mediante `shutil.which`.
- **Firma y notarización:** sin firmar, Gatekeeper bloquea la app («no se puede abrir porque proviene de un desarrollador no identificado»). Opciones:
  - Con cuenta de Apple Developer: firmar con `codesign` y notarizar con `xcrun notarytool`.
  - Sin cuenta: documentar que hay que abrirla con clic derecho → *Abrir*, o ejecutar `xattr -dr com.apple.quarantine BiliDownloader.app`.
- **Distribución:** imagen `.dmg` (con `hdiutil` o `create-dmg`).

#### 5b.5 Automatización con GitHub Actions *(recomendado)*

Un flujo `.github/workflows/build.yml` con una matriz de sistemas compila las tres versiones en cada *tag* de versión y las adjunta a la *release*:

| Runner | Resultado |
|---|---|
| `ubuntu-22.04` | `BiliDownloader-x86_64.AppImage` |
| `windows-latest` | `BiliDownloader-windows-x64.zip` (+ instalador opcional) |
| `macos-latest` (arm64) | `BiliDownloader-macos-arm64.dmg` |
| `macos-13` (Intel, opcional) | `BiliDownloader-macos-x86_64.dmg` |

#### Tareas

- [ ] Aplicar los ajustes comunes de 5b.1.
- [ ] Linux: nuevo script, carpeta *standalone* y AppImage.
- [ ] Windows: actualizar el `.bat`, quitar la petición de administrador y empaquetar en `.zip`.
- [ ] macOS: icono `.icns`, script, `.app` y `.dmg`; decidir si se firma.
- [ ] Documentar la compilación de cada sistema en `SETUP.md`.
- [ ] *(Opcional)* Flujo de GitHub Actions para las tres plataformas.

### Fase 6 — Pruebas funcionales

Probar en **Linux**, **Windows** y **macOS**:

- [ ] La app arranca y se muestra la ventana principal.
- [ ] Entrada por BV, AV, EP, MD y por URL completa.
- [ ] Lectura automática del portapapeles.
- [ ] Inicio de sesión por QR y cierre de sesión.
- [ ] Selección de episodios, resolución y códec.
- [ ] Descarga, pausa, reintento y combinación de audio y video con ffmpeg.
- [ ] Descarga de solo audio y de comentarios en pantalla (danmaku).
- [ ] Guardar la portada (clic derecho).
- [ ] Cambiar el estilo Qt y la opción de alta densidad (DPI), reiniciar y verificar.
- [ ] Ejecutable compilado con Nuitka (Linux y portable de Windows).
- [ ] Linux: AppImage en una sesión **X11** y en una **Wayland** (GNOME y KDE), con y sin `ffmpeg` del sistema.
- [ ] Windows: versión portable **sin** permisos de administrador; Windows 10 y 11.
- [ ] macOS: `.dmg` en Apple Silicon (y en Intel si se da soporte); abrir la app con Gatekeeper activo.

### Fase 7 — Cierre

- [ ] Actualizar `SETUP.md` con las nuevas versiones y los pasos.
- [ ] Añadir una entrada al `CHANGELOG.md`.
- [ ] Commit y, si procede, PR.

---

## 3. Riesgos y mitigación

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Fuentes borrosas con Qt ≥ 6.8 (motivo del retroceso en 1.3.5) | Media | Probar las políticas de redondeo de escala DPI y el *hinting* en la fase 2, en Windows con escalado 125–150 % |
| Cambios de API en PySide6 que rompan widgets | Baja–media | Regenerar la UI y probar pantalla por pantalla |
| Opciones de Nuitka renombradas o eliminadas | Media | Revisar `python -m nuitka --help` antes de compilar |
| Cookies guardadas ilegibles tras actualizar pywin32 | Baja | Probar con un perfil ya existente; si falla, pedir iniciar sesión de nuevo |
| Estilo Qt guardado que ya no existe | Baja | Comprobar `None` antes de `app.setStyle` |
| El AppImage no arranca en distribuciones más antiguas (glibc) | Media | Compilarlo en un contenedor con una distribución antigua con soporte (p. ej. Ubuntu LTS anterior) |
| Faltan complementos de Qt para Wayland en el ejecutable | Media | Probar en Wayland; como reserva, `QT_QPA_PLATFORM=xcb` |
| Gatekeeper bloquea la app en macOS por no estar firmada | Alta (sin cuenta de desarrollador) | Firmar y notarizar, o documentar cómo abrirla |
| No hay equipos Mac o Windows para compilar y probar | Media | Usar los *runners* de GitHub Actions para compilar; las pruebas manuales siguen necesitando el equipo o una VM |

---

## 4. Orden recomendado

1. Fases 0 y 1 (entorno y dependencias).
2. Fase 2 (PySide6): es la que más trabajo tiene; hasta terminarla no vale la pena seguir.
3. Fases 3 y 4.
4. Fase 5b.1 (ajustes de código multiplataforma): se pueden hacer en paralelo con la fase 3.
5. Fases 5 y 5b.2–5b.5 (compilación por sistema y automatización) y fase 6 (pruebas).
6. Fase 7 (documentación y cierre).
