# BiliDownloader

### Copyright © 2021-2026 Majjcom

- 1.4.0 2026/9/19
  - Se actualizó el módulo de descarga de videos. Ahora es más fiable y además admite pausar, reintentar y otras funciones útiles
  - Actualización de componentes base
  - Se corrigió el parpadeo de la barra de progreso tras pulsar el botón de reintentar en una tarea de descarga
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.21 2026/8/14
  - Se corrigió un error al descargar videos de gran tamaño
  - Se optimizó la lógica de inicio de sesión
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.20 2026/8/7
  - Corrección urgente de la sesión caducada y de la imposibilidad de iniciar sesión con normalidad
  - Optimización del código de PySide
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.19 2026/7/8
  - Se añadió soporte para la traducción de voz original con IA
  - Se optimizó la lógica de selección de audio
  - Se actualizó **ffmpeg** a la versión 8.1.2; **esta versión corrige una vulnerabilidad grave presente en el ffmpeg anterior**
  - Se comprime el binario de ffmpeg con upx para reducir el espacio ocupado
  - Actualización de las bibliotecas base
  - ¡Gracias por su apoyo ~


- 1.3.18 2026/1/21
  - Se actualizó ffmpeg y se mejoró el soporte para audio flac
  - Se optimizó la lógica de selección del flujo de audio; ahora se obtiene audio de mayor calidad
  - Se mejoraron los textos descriptivos de los códecs de video
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.17 2026/1/13
  - Se corrigió la imposibilidad de descargar videos sin flujo de audio
  - Se corrigió que, en algunos casos, no se pudieran combinar audio y video al elegir descargar audio flac
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.16 2025/12/6
  - Se corrigió un error de análisis causado por el fallo al obtener la portada de algunos videos
  - Se corrigió el funcionamiento anómalo de algunas funciones con Python 3.8
  - Actualización de componentes base
  - ¡Gracias por su apoyo ~


- 1.3.15 2025/10/10
  - Se corrigió el análisis erróneo de una pequeña parte de los enlaces de video
  - Se corrigió el error 404 que aparecía al activar la `descarga en resolución ultra alta`
  - ¡Gracias por su apoyo ~


- 1.3.14 2025/10/1
  - Se añadió el análisis de **audio Hi-Res** y **audio Dolby**
  - Se añadió en la pantalla de configuración un botón para **abrir el directorio de descargas**
  - La versión portable incluye ahora una variante con Python 3.12; si te interesa, puedes probarla y, si encuentras problemas, reportarlos en el repositorio o en el foro. La versión de Python predeterminada sigue siendo la 3.10
  - Se ajustó la lógica de la opción **leer el portapapeles**, **reduciendo lecturas innecesarias del archivo de configuración**
  - Se ajustó la descripción en la interfaz de la configuración de códec
  - Se ajustó la función del botón de selección de episodios; ahora, al pulsarlo **sin contenido**, se **invierte toda la selección**
  - Se actualizaron las descripciones de resolución; ahora coinciden con las del reproductor web
  - Se corrigió un posible problema de fuentes en la pantalla de configuración
  - Se corrigió el **problema de fuentes en la versión portable**; si la fuente indicada no existe, **se registrará en el sistema**
  - **Si no quieres que el programa registre fuentes, elimina la carpeta font antes del primer inicio**
  - Actualización del componente ffmpeg
  - Actualización de componentes base
  - ¡Gracias por su apoyo ~


- 1.3.13 2025/9/10
  - Se añadió la función de **leer el portapapeles del sistema**, que **rellena automáticamente** el contenido cuando **hay una coincidencia**; se puede desactivar en la configuración
  - Se añadió un aviso para la función de **guardar portada**
  - Se optimizó la entrada de selección de episodios, mejorando el caso de un solo episodio
  - Se mejoró el texto de ayuda de la entrada de selección de episodios
  - Se optimizó la velocidad de desplazamiento en la pantalla de descargas
  - Se corrigió que, en algunos casos, el lanzador no iniciara correctamente el programa principal


- 1.3.12 2025/8/21
  - Se corrigió el cierre inesperado del programa al pulsar el botón de inicio de sesión
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.11 2025/8/18
  - Se añadió compresión en las peticiones a la API para reducir el consumo de ancho de banda
  - Se añadió una compilación portable (Portable); a partir de ahora se publicará también la versión portable en el sitio de descargas
  - Se actualizaron las plantillas de petición, corrigiendo posibles problemas
  - Actualización de componentes base
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.10 2025/6/29
  - Se corrigieron los caracteres ilegibles en la descripción del lanzador
  - Se corrigió que la información de inicio de sesión no se guardara


- 1.3.9 2025/6/29
  - El lanzador se compila con tcc: menor tamaño y compilación más rápida
  - Se mejoró la visualización borrosa de fuentes en pantallas de alta densidad (DPI)
  - Se optimizó la lógica del archivo de configuración
  - Se corrigió el color de fondo inconsistente en la pantalla de configuración
  - Se corrigió que la opción «No volver a mostrar» del aviso de descarga no funcionara
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.8 2025/5/13
  - Se añadió la opción **eliminar el límite de longitud del nombre de archivo** (no se recomienda activarla)
  - Se añadió la función de **cerrar sesión**
  - Se corrigió que, sin conexión, apareciera el aviso de sesión caducada (cuando en realidad no lo estaba)
  - Se corrigieron problemas del módulo de archivo de configuración
  - Se corrigió el fallo al iniciar el paquete de actualización cuando la ruta de descarga contenía espacios
  - Actualización de componentes base
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.7 2025/3/8
  - Se añadió en la configuración la opción **abrir el directorio del archivo de configuración**
  - Se optimizó la lógica de guardado de la configuración, corrigiendo que en algunos casos **no se guardara**
  - Se optimizó la regex con la que el módulo de inicio de sesión obtiene la cookie, evitando posibles problemas
  - La información de la cookie del usuario se cifra según el hardware del equipo, **mejorando la seguridad**
  - *Tras esta actualización, los nuevos inicios de sesión **ya no podrán** transferirse a otros dispositivos modificando el archivo de configuración*
  - Actualización de componentes base
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.6 2025/2/4
  - Se corrigió el orden desordenado de las pestañas (Tab) en la configuración
  - Se corrigió un error en la lógica de caché del compilador de UI
  - La verificación de archivos pasa a usar sha256, mejorando la seguridad
  - Actualización de versiones de componentes base
  - Actualización de la información de copyright
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.5 2024/12/13
  - Se volvió a Qt 6.7 para solucionar las fuentes borrosas cuando no hay adaptación a alta densidad (DPI)


- 1.3.4 2024/12/13
  - Se activó la adaptación a alta densidad (DPI), solucionando una visualización incorrecta en algunos dispositivos
  - Actualización de Python y de los componentes correspondientes
  - Actualización de la versión de la biblioteca Qt
  - Actualización de la versión de Nuitka
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.3 2024/11/9
  - Se añadió la función `descargar solo audio`
  - Se optimizó la ruta del archivo de configuración en Linux
  - Se añadió un script de compilación del ejecutable para Linux
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.2 2024/10/3
  - Se corrigió que en algunos casos el archivo de configuración dejara de ser válido
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.1 2024/7/25
  - Se añadió una opción para cambiar el estilo de la interfaz; el cambio se aplica tras reiniciar
  - La página de configuración ahora es un área desplazable
  - Se añadió un aviso de guardado en la pantalla de configuración
  - Se cambió el orden de algunas opciones de configuración para mejorar la presentación
  - Se mejoró la página de LICENCIA
  - Se optimizó la actualización: si el instalador ya existe y coincide con la huella en la nube, no se vuelve a descargar
  - Optimización del servidor
  - Se corrigió que, tras volver a descargar, pulsar el botón de limpiar completados pudiera eliminar elementos en descarga
  - Se corrigió que se pudiera avanzar al siguiente paso sin seleccionar ningún elemento
  - Se cambió la lógica del botón de reintentar para evitar errores por pulsaciones repetidas
  - Se corrigió que el tamaño del efecto de selección de la lista de descargas no coincidiera con el real
  - Actualización del componente ffmpeg
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.3.0 2024/7/7
  - Se actualizaron los componentes de Qt y se usa una nueva interfaz
  - Se cambió el componente de empaquetado, logrando mayor rendimiento
  - Ligera reducción del tamaño del paquete
  - Se eliminó el soporte para PC de 32 bits
  - A partir de esta versión, los usuarios pueden actualizar de forma selectiva a versiones posteriores a la 1.3.0
  - Consulta la información de cada actualización para decidir si necesitas actualizar
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.2.2 2024/5/31
  - Se añadió una nueva API para gestionar algunos casos especiales
  - Se corrigió la imposibilidad de descargar algunos animes, películas y series
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.2.1 2024/5/18
  - Se añadió la función de guardar la portada del video
  - En la página de confirmación, haz clic derecho sobre la portada para guardarla
  - Se corrigió que la configuración no se restableciera correctamente
  - Se añadió gestión de UAC
  - Se añadieron algunos avisos de descarga
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.2.0 2024/4/13
  - Se añadió soporte para descargar videos en 8K y HDR
  - Inicia sesión con una cuenta con membresía premium (大会员) y activa la opción de resolución ultra alta en la configuración para descargar videos en 8K y HDR
  - Se modificó parte de la interfaz provisional
  - Se añadió información de licencia en la página Acerca de
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.1.1 2024/3/7
  - Se corrigió que los caracteres especiales en el título pudieran afectar al funcionamiento del programa
  - Se añadió soporte parcial para Linux
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.1.0 2024/2/25
  - Se añadió un aviso de sesión caducada
  - La función de descarga puede fallar una vez caducada la sesión
  - Inicia sesión o restablece a tiempo
  - Se cambió la arquitectura del servidor, mejorando estabilidad y velocidad
  - Se optimizó la lógica de lectura de la configuración, reduciendo operaciones innecesarias
  - Gracias por su apoyo


- 1.0.8 2024/2/12
  - Se actualizaron algunas APIs y se añadió la lógica de firma Wbi
  - Actualización del backend de Python
  - Se mejoró en parte la experiencia de descarga
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.0.7 2023/12/14
  - Se corrigió el cierre inesperado al descargar videos grandes
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.0.6 2023/12/4
  - Se corrigió la imposibilidad de iniciar sesión con normalidad
  - Se actualizaron algunas APIs
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.0.5 2023/11/3
  - Se corrigió la imposibilidad de descargar «videos sin puntuación»
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.0.4 2023/10/20
  - Se añadió la selección rápida de episodios en la pantalla de selección
  - Se añadió el prefijo de parte (P) a los videos descargados
  - Optimización de algunas funciones
  - Corrección de algunos problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.0.3 2023/10/6
  - Se añadió el botón `Reintentar descarga`; si la descarga se atasca, puedes intentar reintentarla, aunque puede quedar algún archivo xxx_temp que puedes borrar tras cerrar el programa
  - Se modificaron algunos textos de la interfaz
  - Se añadió el botón `Mostrar CHANGELOG` en la página Acerca de
  - Corrección de algunos problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.0.2 2023/9/23
  - Se corrigió el fallo al descargar usando el número AV
  - Se añadió la opción de descarga de comentarios en pantalla (danmaku) en la configuración
  - Se añadió la visualización del número de espectadores en línea del video
  - Se añadió la página Acerca de, con algo de información
  - Corrección de problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.0.1 2023/9/10
  - Se corrigió el bloqueo de las tareas de descarga
  - Se corrigió que apareciera una ventana de línea de comandos al combinar videos
  - Se mejoró la pantalla de aviso de nueva versión
  - Se añadió una confirmación al restablecer
  - Se optimizó la página de descargas
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 1.0.0 2023/9/6
  - Actualización mayor con numerosas mejoras
  - Se actualizó el núcleo de Python a la 3.10
  - La biblioteca gráfica pasa de TK a Qt5, más atractiva
  - Se actualizaron las vistas de las páginas, más intuitivas
  - Se actualizó la página de selección de episodios, más rápida y cómoda
  - Se añadió la descarga de múltiples tareas
  - Se optimizó la página de vista previa, mejorando la experiencia de uso
  - Se mejoró la experiencia en la página de descargas
  - Optimización del servidor


- 0.13.0 2023/8/15
  - Se actualizó el núcleo de Python a la 3.8.17
  - Se corrigió el error al descargar comentarios en pantalla (danmaku)
  - Se corrigió que algunos números BV especiales pudieran identificarse como números AV y provocar errores
  - Se actualizaron algunas APIs, mejorando la seguridad
  - Parte del código se compila a binario, aumentando la velocidad de ejecución
  - Parte del código principal se transpila, mejorando la seguridad
  - Se mejoró el soporte para PC de 32 bits
  - Corrección de bugs conocidos
  - ¡Gracias por su apoyo ~


- 0.12.6 2023/7/28
  - Se añadió la función de elegir el códec de video; elegir un códec más avanzado reduce eficazmente el tamaño y el tiempo de descarga
  - Se actualizó el componente ffmpeg, con soporte para el códec AV1
  - Se actualizó el componente de API, mejorando eficiencia y seguridad
  - Corrección de bugs conocidos
  - ¡Gracias por su apoyo ~


- 0.12.5 2023/5/27
  - Se corrigió el error al obtener el número de espectadores en línea del video
  - Se cambió el TimeOut a 5 segundos, reduciendo el tiempo de espera


- 0.12.4 2023/1/16
  - Se añadió la función de ver la portada
  - Corrección de bugs conocidos
  - ¡Gracias por su apoyo ~


- 0.12.3 2023/1/10
  - Se actualizó el núcleo de Python a la 3.8.16
  - Corrección de algunos problemas conocidos
  - La próxima vez se intentará añadir la función de ver la portada
  - ¡Gracias por su apoyo ~


- 0.12.2 2022/11/5
  - Se corrigió que no se pudieran descargar algunos videos con caracteres especiales en el título
  - En la pantalla de selección de partes (P) se seleccionan todas por defecto
  - Actualización de componentes principales
  - Corrección de otros problemas conocidos
  - ¡Gracias por su apoyo ~


- 0.12.1 2022/9/22
  - Se corrigió que no se pudieran obtener videos tras iniciar sesión


- 0.12.0 2022/9/22
  - Se añadió la descarga de comentarios en pantalla (danmaku); actívala en la configuración si la necesitas
  - ¡Al confirmar un video, ahora se muestra su número de espectadores en línea!
  - Se reforzó la estabilidad y compatibilidad del servidor
  - Se instalan fuentes durante la instalación para evitar algunos problemas extraños
  - Corrección de problemas conocidos
  - Gracias por su apoyo, ¡gu gu gu~ (perdón por la tardanza)


- 0.11.9 2022/7/8
  - Se corrigió un OSError


- 0.11.8 2022/5/28
  - Se corrigió un problema de seguridad en las llamadas a la API
  - Se intentó corregir que algunas descargas se quedaran atascadas cerca del 99
  - Se cambió la estructura de la API, mejorando la eficiencia
  - Se optimizó el descargador multihilo


- 0.11.7 2022/5/3
  - Ahora se puede introducir directamente la URL del video, ¡sin tener que buscar el número!
  - Se optimizó el módulo de descarga multihilo
  - Optimización del servidor
  - Se mejoraron los avisos de actualización


- 0.11.6 2022/4/22
  - Se optimizó el módulo de descarga multihilo
  - Se compiló el núcleo de Python 3.8.13, mejorando estabilidad y seguridad


- 0.11.5 2022/4/17
  - Se corrigieron posibles problemas del módulo de descarga multihilo
  - Optimización de la interfaz
  - Se añadió en la configuración la opción de conservar el audio; al activarla se conservarán los datos de audio descargados
  - Gracias por su apoyo


- 0.11.4 2022/4/9
  - Se corrigió que no se pudieran descargar algunos videos con caracteres especiales en el título


- 0.11.3 2022/4/3
  - Corrección de algunos posibles problemas
  - Optimización de la estructura
  - La próxima versión secundaria ofrecerá actualización en caliente, con una velocidad de actualización muy rápida


- 0.11.2 2022/2/10
  - Se corrigió un error grave por el que la aplicación no arrancaba si el directorio de descarga no existía
  - Se solucionó el fallo al descargar algunos videos con caracteres especiales en el título
  - Corrección de algunos problemas menores
  - Si encuentras algún problema durante el uso, puedes comentarlo en Coolapk (酷安) o en el grupo de QQ; haremos lo posible por resolverlo
  - P.D. Gracias por su apoyo


- 0.11.1 2022/2/5
  - Se recompiló la biblioteca gráfica, acelerando la generación del código QR
  - Se corrigieron varios problemas causados al cerrar la ventana de inicio de sesión con código QR
  - Todas las llamadas a la API pasan a usar el protocolo `https`, mejorando la seguridad
  - Mensajes de error más detallados, facilitando la depuración
  - Se añadió un botón de ayuda en la pantalla de configuración
  - Se añadió el botón `Abrir directorio de descargas` en la pantalla de finalización
  - Solución de algunos problemas menores
  - Si encuentras algún problema durante el uso, puedes comentarlo en Coolapk (酷安) o en el grupo de QQ; haremos lo posible por resolverlo
  - P.D. Gracias por su apoyo


- 0.11.0 2022/1/31
  - Se añadió la descarga de anime mediante el número `ep`
  - Se añadió el inicio de sesión mediante código QR
  - Se reestructuró la lógica de llamadas a la API, con respuestas más rápidas
  - Se eliminó contenido innecesario, mejorando la eficiencia
  - Se corrigió el parpadeo de la ventana al iniciar
  - Se corrigió la falta de icono en el aviso de actualización
  - Se corrigieron algunos problemas menores de la ventana de aviso de actualización
  - Se modificó parte de la interfaz de las ventanas (sobre todo la ventana de mensajes de error)
  - Se eliminó la opción `pasaporte de Bilibili`, sustituida por el inicio de sesión con código QR
  - Solución de varios problemas menores
  - Si tienes algún problema durante el uso, coméntalo en Coolapk (酷安) o en el grupo de QQ; haremos lo posible por resolverlo
  - P.D. Gracias a todos por su apoyo


- 0.10.7 2022/1/21
  - Se corrigió un error al descargar algunos videos con títulos poco comunes
  - Se añadió la visualización de la información de actualización
  - Te invitamos a unirte al grupo 814913258; introduce el nombre completo de esta aplicación, BiliDownloader, para entrar
  - En el grupo se publican las actualizaciones y puedes preguntar cualquier duda (aunque no siempre habrá alguien)


- 0.10.6 2022/1/15
  - Se corrigió la descarga de anime
  - Se corrigió un error del componente de la ventana de actualización
  - Mejora de la lógica: ya no se cierra la aplicación tras cambiar la carpeta de descargas
  - Se añadió documentación de compilación al repositorio git (en redacción)
  - Se embelleció el formato del archivo de configuración Json
  - Te invitamos a unirte al grupo 814913258; introduce el nombre completo de esta aplicación, BiliDownloader, para entrar


- 0.10.5 2022/1/8
  - Se añadieron algunas operaciones con teclado para facilitar el uso de la aplicación
  - Se recompilaron los componentes principales, reduciendo el tamaño del paquete
  - Te invitamos a unirte al grupo 814913258; introduce el nombre completo de esta aplicación, BiliDownloader, para entrar
  - En el grupo se publican las actualizaciones y puedes preguntar cualquier duda


- 0.10.4 2022/1/1
  - Se modificaron algunos avisos
  - La página de ayuda del pasaporte se trasladó a gitee
  - Se reforzó la estabilidad del servidor


- 0.10.3 2021/12/25
  - Se corrigió la imposibilidad de obtener actualizaciones
  - Los usuarios que no hayan obtenido una versión superior a la 0.10.3 seguirán recibiendo soporte hasta que se solucione el problema del servidor
  - Se reforzó la estabilidad del servidor


- 0.10.2 2021/11/28
  - Se cambió la ubicación de los archivos temporales
  - Se cambió la interfaz de avisos sonoros
  - Se añadió un cuadro de confirmación al restablecer la configuración, para evitar errores
  - Se actualizó de nuevo la arquitectura bdnet, haciendo el desarrollo más rápido y cómodo
  - Se modificó parte de la lógica del código
  - Se añadió la omisión de contenido para miembros, evitando descargas inválidas
  - Se modificó el contenido de los avisos
  - Se cambió el tamaño de los fragmentos de descarga


- 0.10.1 2021/11/27
  - Se pasó a descarga fragmentada multihilo; las descargas de videos grandes ya no se interrumpen a medias
  - Se añadió la función de restablecer la configuración
  - Se habilitó el soporte del protocolo bdnet, con una comprobación de actualizaciones más rápida


- 0.10.0 2021/11/20
  - Se añadió la configuración del pasaporte de Bilibili
  - Haz clic derecho en la página principal para pegar contenido
  - Corrección de BUGs conocidos


- 0.9.4 2021/11/6
  - Se modificó la interfaz de la página principal
  - Se añadió un acceso a la configuración en la página principal para ajustar opciones con más comodidad (por ejemplo, la ruta)
  - Se modificó parte de la lógica del código
  - En la próxima versión mayor se prevé reescribir el protocolo de red, lo que mejorará enormemente la estabilidad y la seguridad
  - La próxima versión mayor incluirá la configuración del pasaporte de Bilibili; quienes tengan membresía premium (大会员) podrán usar su cuenta para descargar contenido de pago


- 0.9.3 2021/10/31
  - Se añadió un cuadro de aviso de comprobación de actualizaciones
  - Ajustes de detalle para que el descargador sea más fácil de usar
  - Se modificó parte de la interfaz


- 0.9.2 2021/10/24
  - Se mejoró la estructura del código para que la depuración sea más cómoda
  - Se añadió un aviso de ubicación de descarga, más práctico
  - Se añadieron algunos sonidos de aviso


- 0.9.1 2021/10/17
  - Se recompiló ffmpeg 3.0, reduciendo el tamaño del paquete


- 0.9.0 2021/10/16
  - Actualización de la interfaz; esta vez con cambios grandes y un aspecto más agradable
  - Se admite cambiar la ubicación de guardado de las descargas
  - Cambios importantes en la estructura del código
  - Modificación de avisos
  - Corrección de algunos BUGs conocidos
