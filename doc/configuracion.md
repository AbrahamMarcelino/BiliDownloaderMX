# Configuración y datos del usuario

Toda la configuración se guarda en `data/userdata.json`, dentro del directorio de trabajo (ver [arquitectura](arquitectura.md#directorio-de-trabajo)). La gestiona `src/utils/configUtils.py`.

## Formato

```json
{
  "isnew": false,
  "version": "1.4.0",
  "userinfo": {
    "downloadPath": "D:/Videos",
    "video_codec": 13,
    "passport": { "ts": 1790000000, "secure_data": "…" },
    "passport_crypt_key": "…"
  }
}
```

- `version` e `isnew` sirven para mostrar el changelog en la primera ejecución o tras actualizar (`utils/init.py`).
- Las preferencias viven en `userinfo`. Si una clave no existe, se usa el valor por defecto.

## Claves (`configUtils.Configs`)

| Clave | Constante | Por defecto | Pantalla | Descripción |
|---|---|---|---|---|
| `downloadPath` | `DOWNLOAD_PATH` | `Download/` (absoluta) | Carpeta de descargas | Carpeta de descarga |
| `video_codec` | `VIDEO_CODEC` | `7` (H.264) | Códec preferido | Códec preferido: 7 AVC, 12 HEVC, 13 AV1 |
| `max_thread_count` | `MAX_THREAD_COUNT` | `4` | Descargas simultáneas | Descargas simultáneas (requiere reiniciar) |
| `qt_ui_style` | `QT_STYLE` | `"default"` | Estilo de la interfaz | Estilo Qt (`Fusion`, `windows11`…; requiere reiniciar) |
| `reserveAudio` | `RESERVE_AUDIO` | `false` | Conservar el audio descargado | Conservar el audio además del video |
| `ultra_resolution` | `ULTRA_RESOLUTION` | `false` | Activar resolución ultra alta | Pedir 8K y HDR (requiere membresía premium) |
| `pull_dolby_audio` | `PULL_DOLBY_AUDIO` | `false` | Obtener audio Dolby | Pedir pistas Dolby |
| `disable_title_length_limit` | `DISABLE_TITLE_LENGTH_LIMIT` | `false` | Quitar el límite de longitud del nombre | No recortar nombres a 20 caracteres (no recomendado) |
| `apply_high_dpi` | `APPLY_HIGH_DPI` | `true` | Adaptar a pantallas de alta densidad (DPI) | Si es `false`, se define `QT_ENABLE_HIGHDPI_SCALING=0` (requiere reiniciar) |
| `download_audio_only` | `DOWNLOAD_AUDIO_ONLY` | `false` | Descargar solo audio | Valor inicial de la casilla «solo audio» |
| `saveDanmaku` | `SAVE_DANMAKU` | `false` | Descargar danmaku (comentarios) | Valor inicial de la casilla «danmaku» |
| `auto_fill_data_from_clipboard` | `AUTO_FILL_DATA_FROM_CLIPBOARD` | `true` | Leer el portapapeles automáticamente | Rellenar la entrada con el portapapeles al activar la ventana |
| `show_download_tip` | `SHOW_DOWNLOAD_TIP` | `true` | (casilla «No volver a mostrar» del aviso) | Mostrar el aviso «añadido a la cola» |
| `passport` | `PASSPORT` | — | Sesión de Bilibili | Sesión cifrada: `ts` (caducidad) y `secure_data` |
| `passport_crypt_key` | `PASSPORT_CRYPT_KEY` | — | — | Clave de la sesión (protegida con DPAPI en Windows) |

La pantalla de configuración guarda los cambios **al salir de la pestaña** (lo indica el texto animado «Sal de esta pestaña para guardar los cambios») o al cerrar la ventana. También tiene botones para abrir la carpeta de configuración, abrir la de descargas y restablecer toda la configuración.

## API de `configUtils`

| Función / clase | Uso |
|---|---|
| `getUserData(clave, por_defecto)` | Lee **todo el archivo** en cada llamada y devuelve un valor |
| `setUserData(clave, valor)` | Lee, modifica y reescribe el archivo. `valor=None` borra la clave |
| `UserDataHelper(autosave=False)` | Carga el archivo una vez; `get`, `set`, `save` (solo si hubo cambios) y `reload` |
| `setupUserData()` | Crea `data/` y un `userdata.json` vacío si no existen |
| `reSetUserData()` | Borra y recrea el archivo (botón «restablecer») |

## Migrar la configuración

Copiar la carpeta `data/` al nuevo directorio de trabajo conserva las preferencias. La **sesión** solo sigue siendo válida en el mismo equipo y usuario de Windows, porque la clave está protegida con DPAPI (ver [guía de usuario](guia-de-usuario.md#migrar-la-configuración-a-una-versión-nueva)).
