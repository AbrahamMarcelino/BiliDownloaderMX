from PySide6 import QtWidgets, QtGui

from coloredlabel import ColoredLabel

reactions = (
    "¿Por qué me das clic?",
    "Ya estuvo",
    "¿Será que me das clic porque me veo bien?",
    "¿Todavía sigues dando clic?",
    "¡Aaaaaah!",
    "Ya no le des clic",
    "Aquí no hay nada",
    "Ya te ha de doler la mano",
    "Oye, ¿en serio sigues dando clic?",
    "Bueno, ya no juego contigo, me voy",
    "No, ahora sí me voy",
    "Por más clics que des, nadie te va a pagar",
    "Ya, ya",
    "¿Por qué tanta insistencia?",
    "Ya no juego, ahora sí me voy. Bye~~~",
)


class SpecialColoredLabel(ColoredLabel):
    def __init__(self, parent: QtWidgets.QWidget = ...):
        super().__init__(parent)
        self.click_times = 0
        self.re_index = 0

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        super().mousePressEvent(event)
        if event.isBeginEvent():
            self.click_times += 1
        if self.click_times % 16 == 0 and self.re_index < len(reactions):
            QtWidgets.QMessageBox.information(self.parent(), "¿Qué pasa?", reactions[self.re_index])
            self.re_index += 1
            self.click_times = 0
        if self.re_index >= len(reactions):
            self.deleteLater()
