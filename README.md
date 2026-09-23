# BiliDownloader

![tag](https://img.shields.io/badge/Language-Python3,_C++-orange.svg) ![tag](https://img.shields.io/badge/License-MIT-green.svg)

> **Nota:** este repositorio es una adaptación al **español latino** del proyecto original [Majjcom/BiliDownloader](https://github.com/Majjcom/BiliDownloader), creado por Majjcom. Todo el crédito del desarrollo corresponde a su autor original; aquí solo se traduce la documentación para que la comunidad hispanohablante pueda usarlo con mayor facilidad.

## Introducción

Este es un descargador de videos de Bilibili (b站) de código abierto

## Uso

En Windows basta con instalar la versión publicada (release) para usarlo

Introduce un número BV, AV, MD o EP para obtener el video (el número MD es el **mdxxxx** que aparece en el enlace de la página de detalles de un anime/serie)

![](imgs/2026-09-20_17-55-14.png)

------

Puedes configurar la <u>ubicación de descarga</u> en la **pantalla de configuración**

En algunos casos, necesitarás iniciar sesión con tu cuenta de Bilibili mediante código QR desde la pantalla de configuración para descargar ciertos contenidos exclusivos para miembros

***Esta aplicación no ofrece la descarga directa de contenido exclusivo para miembros. Si deseas descargar dicho contenido, inicia sesión con una cuenta que tenga membresía premium (大会员) y realiza la descarga***

------

Tras confirmar la información, elige los episodios; marca la casilla de la izquierda para descargarlos

------

En la siguiente página, elige la resolución y el códec de video; aquí también puedes cambiar temporalmente la ruta de guardado

------

Después, haz clic en enviar para iniciar la descarga

------

## Documentación

- [Guía de usuario](doc/guia-de-usuario.md): versiones disponibles, migración de la configuración, uso paso a paso y glosario de la interfaz (traducida de la publicación del autor en el foro 52pojie)
- [Guía de compilación](SETUP.md)
- [Documentación técnica](doc/README.md): arquitectura, API de Bilibili, motor de descargas, configuración y revisión de código
- [Plan de migración a bibliotecas actuales](doc/plan-migracion-dependencias.md)
- [Historial de cambios](CHANGELOG.md)

## Notas

Por ahora no se ofrece la descarga de contenido con **audio Dolby**

Algunos videos requieren **membresía premium (大会员)** para descargarse completos; inicia sesión con tu cuenta en <u>**Configuración**</u>

Algunas resoluciones requieren **membresía premium (大会员)** para descargarse; inicia sesión en la configuración

## Otros

El ejecutable de Windows se compila con Nuitka

## Capturas de pantalla

![](imgs/2026-09-20_17-58-32.png)

![](imgs/2026-09-20_17-58-40.png)

![](imgs/2026-09-20_17-59-18.png)



Nota final: agradecimientos al [foro 吾爱破解 (52pojie)](www.52pojie.cn)

maj001@www.52pojie.cn
