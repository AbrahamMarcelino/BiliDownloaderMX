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
| `downloadPath` | `DOWNLOAD_PATH` | `Download/` (absoluta) | 默认保存位置 | Carpeta de descarga |
| `video_codec` | `VIDEO_CODEC` | `7` (H.264) | 默认优选编码 | Códec preferido: 7 AVC, 12 HEVC, 13 AV1 |
| `max_thread_count` | `MAX_THREAD_COUNT` | `4` | 最大下载线程数 | Descargas simultáneas (requiere reiniciar) |
| `qt_ui_style` | `QT_STYLE` | `"default"` | 设置UI风格 | Estilo Qt (`Fusion`, `windows11`…; requiere reiniciar) |
| `reserveAudio` | `RESERVE_AUDIO` | `false` | 保留下载的音频文件 | Conservar el audio además del video |
| `ultra_resolution` | `ULTRA_RESOLUTION` | `false` | 启用超高分辨率下载 | Pedir 8K y HDR (requiere membresía premium) |
| `pull_dolby_audio` | `PULL_DOLBY_AUDIO` | `false` | 启用杜比音频解析 | Pedir pistas Dolby |
| `disable_title_length_limit` | `DISABLE_TITLE_LENGTH_LIMIT` | `false` | 解除文件名长度限制 | No recortar nombres a 20 caracteres (no recomendado) |
| `apply_high_dpi` | `APPLY_HIGH_DPI` | `true` | 启用高DPI适配 | Si es `false`, se define `QT_ENABLE_HIGHDPI_SCALING=0` (requiere reiniciar) |
| `download_audio_only` | `DOWNLOAD_AUDIO_ONLY` | `false` | 仅下载音频 | Valor inicial de la casilla «solo audio» |
| `saveDanmaku` | `SAVE_DANMAKU` | `false` | 下载弹幕 | Valor inicial de la casilla «danmaku» |
| `auto_fill_data_from_clipboard` | `AUTO_FILL_DATA_FROM_CLIPBOARD` | `true` | 自动读取剪贴板 | Rellenar la entrada con el portapapeles al activar la ventana |
| `show_download_tip` | `SHOW_DOWNLOAD_TIP` | `true` | (casilla «不再提醒» del aviso) | Mostrar el aviso «añadido a la cola» |
| `passport` | `PASSPORT` | — | 登录B站 | Sesión cifrada: `ts` (caducidad) y `secure_data` |
| `passport_crypt_key` | `PASSPORT_CRYPT_KEY` | — | — | Clave de la sesión (protegida con DPAPI en Windows) |

La pantalla de configuración guarda los cambios **al salir de la pestaña** (lo indica el texto animado «离开设置界面以保存设置») o al cerrar la ventana. También tiene botones para abrir la carpeta de configuración (打开配置文件目录), abrir la de descargas (打开下载目录) y restablecer todo (重置设置).

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
