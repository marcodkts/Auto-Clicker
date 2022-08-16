from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

version = "1.0"


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 400, 150)
        self.setWindowTitle(f"WolfGear AutoClicker v{version}")
        self.init_ui()

    def init_ui(self):
        # noinspection PyAttributeOutsideInit
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Please set a Toggle Key")
        self.label.move(10, 10)
        self.label.adjustSize()

        # noinspection PyAttributeOutsideInit
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Save Toggle Key")
        self.b1.adjustSize()
        self.b1.move(50, 50)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Toggle Key Saved")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()