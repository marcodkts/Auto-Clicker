import sys
from PyQt5 import QtWidgets
from clicker import AutoClicker
from tools import alreadyRunning
from auto_clicker_UI import Ui_form

alreadyRunning()

version = "1.0.0"
clicker = AutoClicker()


class ExtendedFormUI(Ui_form):
    def initForm(self):
        self.LblFooterBuild.setText(f"build v{version}")
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
    with open("gui.css") as style:
        app.setStyleSheet(style.read())
    form = QtWidgets.QWidget()
    ui = ExtendedFormUI()
    ui.setupUi(form)
    form.show()
    ui.initForm()
    sys.exit(app.exec_())
