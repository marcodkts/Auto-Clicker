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


def addConnectors(self):
    self.BtnStart.clicked["bool"].connect(self.startClicker)


Ui_form.addConnectors = addConnectors

def startClicker(self, isPressed: bool) -> None:
    clicker.startClicker(self.LneToggleKey.text())
    self.BtnStart.setText("Stop" if isPressed else "Start")

Ui_form.startClicker = startClicker

def ExecAllExtFunctions(self):
    self.addConnectors()


Ui_form.ExecAllExtFunctions = ExecAllExtFunctions

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(form)
    form.show()
    ui.ExecAllExtFunctions()
    sys.exit(app.exec_())
