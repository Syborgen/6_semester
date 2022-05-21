from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from view.authorization_ui import Ui_AuthorizationForm


class AuthorizationForm(QWidget, Ui_AuthorizationForm):
    logined = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.logIn_button.clicked.connect(self.logIn_button_click)

    def logIn_button_click(self):
        self.logined.emit(self.login_line.text(), self.password_line.text())


# from PyQt5.QtWidgets import *
# import sys

# app = QApplication(sys.argv)

# w = AuthorizationForm()
# w.show()

# sys.exit(app.exec())
