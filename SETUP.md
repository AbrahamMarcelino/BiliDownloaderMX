# Guía de compilación de BiliDownloader

## 1. Ejecutar directamente los archivos .py

### Preparar el entorno de ejecución
Versión de Python >= 3.10

Sistema operativo >= Windows 10

### Instalación rápida de dependencias
Descargar el código
```shell
git clone https://gitee.com/majjcom/bili-downloader.git
```
Se recomienda crear un entorno virtual
```shell
python3 -m venv ./venv

# Activar el entorno virtual; hay que ejecutarlo cada vez que se use
# Por comodidad, puedes no usar un entorno virtual
./venv/Scripts/activate
```

```shell
pip install -r requirements.txt
```

En Windows es necesario instalar bibliotecas adicionales para poder ejecutarlo:

```shell
# Instalar dependencias de Windows
pip install -r requirements_win.txt
```



### Preparativos antes de ejecutar
Descarga el ejecutable de [ffmpeg](https://majjcom.lanzouo.com/b01xc9emh) con soporte para AV1 y extrae `ffmpeg.exe` en el directorio `ffmpeg`, al mismo nivel que `src` (puede que tengas que crear este directorio tú mismo)

Contraseña del enlace: 5ytb

La estructura de directorios queda más o menos así:

```
/--src/--main.py
 |     |-requirments.txt
 |-ffmpeg/--ffmpeg.exe
 |-...
```

El repositorio oculta la clave del servicio; puedes usar el modo sin conexión con las siguientes modificaciones:

Añade `const.py` en `src/Lib/bd_client` con el siguiente contenido:
```python
CONST_KEY=""
```

Modifica `src/update.py` y establece `NO_UPDATE` en True



### Ejecutar
Ejecuta los siguientes comandos en el directorio principal
```shell
cd src
python compile_ui.py
cd ..
pythonw src/main.py
```
Por supuesto, también puedes escribir un script de shell para iniciarlo rápidamente; no se explica aquí, basta con tomar como referencia los comandos anteriores



## 2. Compilar un ejecutable independiente en Linux

### Preparar el entorno de compilación

Primero prepara el entorno de ejecución básico según lo descrito arriba.

Después instala la herramienta de compilación nuitka:

```shell
python -m pip install -U pip
pip install nuitka
```



### Compilar

Es posible que la compilación requiera el paquete `patchelf`; instálalo por tu cuenta

```shell
cd src
python compile_ui.py
chmod +x ./build_nuitka_linux.sh
./build_nuitka_linux.sh
```

El resultado de la compilación se genera en el directorio `dist.nuitka.linux`
