from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog
from view.main_ui import Ui_mainForm
from authorization import AuthorizationForm
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import mimetypes


def attach_file(filepath, msg):
    filename = os.path.basename(filepath)

    ctype, enc = mimetypes.guess_type(filepath)

    maintype, subtype = ctype.split('/', 1)

    with open(filepath, 'rb') as fp:
        file = MIMEBase(maintype, subtype)
        file.set_payload(fp.read())

    encoders.encode_base64(file)
    file.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(file)


class MainForm(QWidget, Ui_mainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.authorization = AuthorizationForm()
        self.authorization.logined.connect(self.check_logIn)

    def initUi(self):
        self.attach_button.clicked.connect(self.attach_button_clicked)
        self.clear_button.clicked.connect(self.clear_button_clicked)
        self.logOut_button.clicked.connect(self.logOut_button_clicked)
        self.send_button.clicked.connect(self.send_button_clicked)

    def send_button_clicked(self):
        msg = MIMEMultipart()
        msg.encoding = 'utf-8'
        msg['Subject'] = Header(self.subject_line.text())
        msg['From'] = Header(self.login)
        msg['To'] = Header(self.to_line.text())
        msg.attach(
            MIMEText(self.message_text.toPlainText(), 'plain', 'utf-8'))
        for i in range(0, self.files_list.count()):  # attach files from list
            item = self.files_list.item(i)
            attach_file(item.text(), msg)
        try:
            self.connect.sendmail(
                self.login, self.to_line.text().split(' '), msg.as_string())
        except:
            QMessageBox.warning(self, 'Ошибка', 'Проверте правильность набора')

    def logOut_button_clicked(self):
        self.connect.quit()
        self.close()
        self.authorization.show()

    def clear_button_clicked(self):
        self.files_list.clear()

    def attach_button_clicked(self):
        filepath = QFileDialog.getOpenFileName(self, 'Выберите файл')[0]
        self.files_list.addItem(filepath)

    def start(self):
        self.authorization.show()

    def check_logIn(self, login, password):
        try:
            self.connect = smtplib.SMTP('smtp.gmail.com', 587)
            self.connect.starttls()
            self.connect.login(login, password)
        except smtplib.SMTPAuthenticationError:
            QMessageBox.warning(self, 'Ошибка авторизации',
                                'Неверный логин или пароль')
        except:
            QMessageBox.warning(self, 'Ошибка авторизации',
                                'Введите корректный логин и пароль')
        else:
            self.login = login
            self.authorization.close()
            self.show()


if __name__ == '__main__':
    from PyQt5.QtWidgets import *
    import sys

    app = QApplication(sys.argv)

    w = MainForm()
    w.show()

    sys.exit(app.exec())
