import pickle

from PySide6 import QtWidgets, QtCore

from centralcheckbox import CentralCheckBox
from ui_selectionwidget import Ui_SelectionWidget

SELECTTON_HELP = """Escribe los episodios que quieres descargar:
Indica cada tramo con un número de episodio o con el formato A-B (inicio y fin), y separa los tramos con comas (,).
Si dejas el campo vacío y presionas «Aplicar selección», se invierte la selección actual.

Ejemplos:
Para descargar la parte 1 y la parte 2, escribe: 1-2 o bien 1, 2

Para descargar de la parte 1 a la 5 sin la 3, divídelo en dos tramos: 1-2, 4-5

Por último, presiona el botón «Aplicar selección» para confirmar."""


class SelectionWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = ...) -> None:
        super().__init__(parent)
        self.ui = Ui_SelectionWidget()
        self.ui.setupUi(self)
        self.meta = None
        self.data = None
        self.ui.button_setSelection.clicked.connect(self.on_set_button_clicked)
        self.ui.button_help.clicked.connect(self.on_help_button_clicked)

    def data_update(self, back):
        if back:
            return
        self.ui.table_selection.setRowCount(0)
        self.ui.button_next.setEnabled(True)
        self.meta: QtCore.QByteArray = self.parent().input_pages[1].meta
        self.data = pickle.loads(self.meta.data())
        for i in self.data["page_data"]:
            box = CentralCheckBox()
            box.get_box().setChecked(True)
            i["box"] = box
            box.get_box().toggled.connect(self.on_check_button_changed)
            item_text = QtWidgets.QTableWidgetItem(i["name"])
            self.ui.table_selection.setRowCount(self.ui.table_selection.rowCount() + 1)
            self.ui.table_selection.setCellWidget(
                self.ui.table_selection.rowCount() - 1, 0, box
            )
            self.ui.table_selection.setItem(
                self.ui.table_selection.rowCount() - 1, 1, item_text
            )

    @QtCore.Slot(bool)
    def on_check_button_changed(self, _checked: bool):
        count = 0
        for i in self.data["page_data"]:
            box = i["box"]
            box = box.get_box()
            if box.isChecked():
                count += 1
        self.ui.button_next.setEnabled(count > 0)

    @QtCore.Slot()
    def on_help_button_clicked(self):
        QtWidgets.QMessageBox.information(self, "Ayuda de selección", SELECTTON_HELP)

    @QtCore.Slot()
    def on_set_button_clicked(self):
        selection_str = self.ui.line_selection.text()

        # Defult to select all
        if len(selection_str) == 0:
            for i in self.data["page_data"]:
                tmp = i["box"].get_box()
                tmp.setChecked(not tmp.isChecked())
            return

        selection_str = selection_str.replace(" ", "")
        selections = selection_str.split(",")
        selected = []
        select_max = -1
        if len(selections) == 0:
            QtWidgets.QMessageBox.critical(self, "Error", "Formato incorrecto")
            return
        for block in selections:
            if '-' in block:
                rng = block.split('-')
                if len(rng) != 2:
                    QtWidgets.QMessageBox.critical(self, "Error", "Formato incorrecto")
                    return
                if not rng[0].isdigit() or not rng[1].isdigit():
                    QtWidgets.QMessageBox.critical(self, "Error", "Formato incorrecto")
                    return
                if int(rng[0]) < 1:
                    QtWidgets.QMessageBox.critical(self, "Error", "Formato incorrecto")
                    return
                if int(rng[0]) > int(rng[1]):
                    QtWidgets.QMessageBox.critical(self, "Error", "Formato incorrecto")
                    return
                if int(rng[1]) > len(self.data["page_data"]):
                    QtWidgets.QMessageBox.critical(self, "Error", "El número de episodio es mayor que el total")
                    return
                if int(rng[0]) <= select_max:
                    QtWidgets.QMessageBox.critical(self, "Error", "Los tramos deben ir en orden ascendente y sin repetirse")
                    return
            else:
                if not block.isdigit():
                    QtWidgets.QMessageBox.critical(self, "Error", "El episodio debe ser un número")
                    return
                if int(block) < 1:
                    QtWidgets.QMessageBox.critical(self, "Error", "Formato incorrecto")
                    return
                if int(block) > len(self.data["page_data"]):
                    QtWidgets.QMessageBox.critical(self, "Error", "El número de episodio es mayor que el total")
                    return
                if int(block) <= select_max:
                    QtWidgets.QMessageBox.critical(self, "Error", "Los tramos deben ir en orden ascendente y sin repetirse")
                    return
                rng = [int(block)] * 2

            for i in range(int(rng[0]) - 1, int(rng[1])):
                selected.append(i)
                select_max = i

        for i in self.data["page_data"]:
            i["box"].get_box().setChecked(False)

        for i in selected:
            self.data["page_data"][i]["box"].get_box().setChecked(True)
