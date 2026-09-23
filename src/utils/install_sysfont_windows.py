import ctypes
import os
import sys

if sys.platform == "win32":
    import winreg as _winreg


def check_font(name: str):
    if _winreg is None:
        return False
    try:
        with _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts") as key:
            i = 0
            while True:
                try:
                    read_name, data, _ = _winreg.EnumValue(key, i)
                    if name.lower() in read_name.lower():
                        return True
                    i += 1
                except OSError:
                    break
    except Exception as e:
        print(f"Error al leer las fuentes instaladas: {e}")
    return False


def install_font(font_name: str, path: str):
    if _winreg is None:
        return False
    if not os.path.exists(path):
        return False
    WINDIR = os.getenv("WINDIR")
    font_path = os.path.split(path)[1]
    if not os.path.exists(f"{WINDIR}\\Fonts\\{font_path}"):
        command = f"XCOPY \"{path}\" {WINDIR}\\Fonts /Y"
        os.system(command)
    value_name = f"{font_name} (TrueType)"
    try:
        with _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts", 0,
                             _winreg.KEY_SET_VALUE | _winreg.KEY_WOW64_64KEY) as key:
            _winreg.SetValueEx(key, value_name, 0, _winreg.REG_SZ, font_path)
    except Exception as e:
        print(f"Error al registrar la fuente: {e}")
        return False

    # Notificar al sistema
    try:
        HWND_BROADCAST = 0xFFFF
        WM_FONTCHANGE = 0x001D
        ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_FONTCHANGE, 0, 0)
        # print("Se notificó al sistema el cambio de fuentes")
    except Exception as e:
        print(f"Error al notificar al sistema el cambio de fuentes: {e}")
        return False

    return True


def test():
    print(ctypes.windll.shell32.IsUserAnAdmin())
    print(check_font("HarmonyOS Sans SC"))
    if install_font("HarmonyOS Sans SC Test", "font\\HarmonyOS_Sans_SC_Regulara.ttf"):
        print("Fuente registrada correctamente")
    else:
        print("No se pudo registrar la fuente")


if __name__ == "__main__":
    test()
