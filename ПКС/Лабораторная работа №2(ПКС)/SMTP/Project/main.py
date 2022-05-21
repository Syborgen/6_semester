from PyQt5.QtWidgets import QApplication
import sys
from mainForm import MainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainForm()
    window.start()
    sys.exit(app.exec())
