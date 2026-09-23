import os
import sys

from PySide6 import QtWidgets


def open_folder(path, qtparent=None):
    if sys.platform == "linux":
        if qtparent is not None:
            QtWidgets.QMessageBox.information(qtparent, "Información", "Esta función aún no está disponible en Linux")
        return
    os.startfile(path, "explore")
