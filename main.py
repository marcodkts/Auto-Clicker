import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from clicker import AutoClicker
from tools import alreadyRunning

alreadyRunning()

version = "2.0.0"
clicker = AutoClicker()

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 400, 140)
        self.setWindowTitle(f"WolfGear AutoClicker v{version}")
        self.initUI()

    def initUI(self):
        # Label
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Please set a Toggle Key")
        self.label.move(10, 10)
        self.label.adjustSize()

        # Textbox
        self.textbox = QLineEdit(self)
        reg_ex = QRegExp("[0-9a-û]")
        input_validator = QRegExpValidator(reg_ex, self.textbox)
        self.textbox.setValidator(input_validator)
        self.textbox.move(10, 40)
        self.textbox.resize(40, 40)

        # Button 1
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Save Toggle Key")
        self.b1.adjustSize()
        self.b1.move(10, 100)

        # Button 1 Action
        self.b1.clicked.connect(self.setToggleKey)

        # Button 2
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Run Auto Clicker")
        self.b2.adjustSize()
        self.b2.move(120, 100)

        # Button 2 Action
        self.b2.clicked.connect(self.runClicker)

    def setToggleKey(self):
        self.label.setText(f"Toggle Key Saved as: {self.textbox.text().upper()}")
        self.textbox.setText("")
        self.update()

    def runClicker(self):
        self.b2.setText("Stop Auto Clicker")
        # clicker.startClicker(self.textbox.text())
        self.update()

    def update(self):
        self.label.adjustSize()
        self.b2.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
