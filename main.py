import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from clicker import AutoClicker
from tools import alreadyRunning
from auto_clicker_UI import Ui_form

alreadyRunning()

version = "2.0.0"
clicker = AutoClicker()

class ExtendedFormUI(Ui_form):
    def addConnectors(self):
        self.BtnStart.clicked["bool"].connect(self.startClicker)
        self.BtnSave.clicked["bool"].connect(self.saveClicker)

    def startClicker(self, isPressed: bool) -> None:
        self.BtnStart.setText("Stop" if isPressed else "Start")
        if isPressed:
            clicker.startClicker(self.LneToggleKey.text())
        else:
            clicker.stopClicker()

    def saveClicker(self, isPressed: bool) -> None:
        self.BtnSave.setText("Edit" if isPressed else "Save")



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = ExtendedFormUI()
    ui.setupUi(form)
    form.show()
    ui.addConnectors()
    sys.exit(app.exec_())
