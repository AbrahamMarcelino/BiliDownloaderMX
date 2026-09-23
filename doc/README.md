# Documentación de BiliDownloader

## Para usuarios

- [Guía de usuario](guia-de-usuario.md): versiones, instalación, uso paso a paso y glosario de la interfaz en chino de las versiones oficiales.

## Para desarrolladores

| Documento | Contenido |
|---|---|
| [Arquitectura](arquitectura.md) | Estructura del repositorio, arranque, pantallas, hilos y archivos que genera la app |
| [API de Bilibili y servicios externos](api-bilibili.md) | Endpoints, firma WBI, banderas `fnval`, inicio de sesión por QR, cifrado de la sesión, danmaku y servidor de actualizaciones |
| [Motor de descargas](motor-de-descargas.md) | Cola, estados, DASH/MP4, reanudación, reintentos y ffmpeg |
| [Configuración](configuracion.md) | Claves de `data/userdata.json` y sus valores por defecto |
| [Revisión de código](revision-de-codigo.md) | Errores encontrados, seguridad, licencias y mejoras sugeridas |
| [Plan de migración](plan-migracion-dependencias.md) | Paso a Python 3.14 y bibliotecas actuales; compilación para Linux, Windows y macOS |
| [Guía de compilación](../SETUP.md) | Cómo ejecutar y compilar el proyecto hoy |

Los diagramas usan [Mermaid](https://mermaid.js.org/); GitHub los muestra directamente.
