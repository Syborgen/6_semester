# cd/d E:/projects/python
# python PKS_lab_2.py
# -*- coding: utf-8 -*-
import smtplib
import poplib
import imaplib
import os
import mailparser
import base64
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime, date, time
while True:
    print("Соединение установлено, выберите команду:")
    print("0. Выход")
    print("1. Отправить сообщение (SMTP)")
    print("2. Отправить сообщение с вложением (SMTP)")
    print("3. Скачать сообщения(POP3)")
    print("4. Скачать сообщения(IMAP)")
    print("5. Прочитать сообщения(IMAP)")
    operation = input("Команда: ")
    if operation == '1':
        subject = input("Введите тему письма: ")
        text = input("Введите текст письма: ")
        server = 'smtp.gmail.com'
        user = 'trisistest11@gmail.com'
        password = 'qwerty123_'
        recipients = ["trisis11@rambler.ru", "trisistest11@gmail.com"]
        sender = "trisis11@rambler.ru"
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg.encoding = 'utf-8'
        part_text = MIMEText(text, 'plain')
        msg.attach(part_text)
        mail = smtplib.SMTP(server, 587)
        mail.starttls()
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
    elif operation == '2':
        subject = input("Введите тему письма: ")
        text = input("Введите текст письма: ")
        filepath = input("Введите имя файла: ")
        server = 'smtp.gmail.com'
        user = 'trisistest11@gmail.com'
        password = 'qwerty123_'
        recipients = ["trisis11@rambler.ru", "trisistest11@gmail.com"]
        sender = "trisis11@rambler.ru"
        basename = os.path.basename(filepath)
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg.encoding = 'utf-8'
        part_text = MIMEText(text, 'plain')
        part_file = MIMEBase(
            'application', 'octet-stream; name="{}"'.format(basename))
        part_file.set_payload(open(filepath, "rb").read())
        part_file.add_header('Content-Disposition',
                             'attachment', filename=basename)
        encoders.encode_base64(part_file)
        msg.attach(part_text)
        msg.attach(part_file)
        mail = smtplib.SMTP(server, 587)
        mail.starttls()
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()
    elif operation == '3':
        server = 'pop.gmail.com'
        port = '995'
        user = 'trisistest11@gmail.com'
        password = 'qwerty123_'
        box = poplib.POP3_SSL(server, port)
        box.user(user)
        box.pass_(password)
        lst = box.list()
        print("DEBUG: Total %s messages: %s" % (user, len(lst[1])))

        for msgnum, msgsize in [i.decode().split() for i in lst[1]]:
            resp, lines, octets = box.retr(msgnum)
            msgtext = b"\n".join(lines) + b"\n\n"
            pmail = mailparser.parse_from_bytes(msgtext)
            t = datetime.now().strftime("%m-%y-%d=%H-%M-%S")
            filename = f'POP3/{msgnum}_{t}.txt'
            print(filename)
            file = open(filename, 'w')
            file.write('')
            file.close()
            file = open(filename, 'a')
            
            file.write(f"От кого: {' '.join(pmail.from_[0])}\n")
            file.write(f"Тема: {pmail.subject}\n")
            file.write(f"Текст сообщения:\n{pmail.text_plain}\n")
            file.write('Файлы:'+ ' '.join([attfile['filename'] for attfile in pmail.attachments]))
            print(f"От кого: {' '.join(pmail.from_[0])}")
            print(f"Тема: {pmail.subject}")
            print(f"Текст сообщения:\n{pmail.text_plain}")
            print('Файлы:', ' '.join([attfile['filename'] for attfile in pmail.attachments]))
            pmail.write_attachments('POP3/attachments')
                # print(msg)
            print()
            file.close()
        box.quit()
    elif operation == '4':
        server = 'imap.gmail.com'
        port = '993'
        user = 'trisistest11@gmail.com'
        password = 'qwerty123_'
        box = imaplib.IMAP4_SSL(server, port)
        box.login(user, password)
        lst = box.list()
        box.select("inbox")
        result, data = box.search(None, "ALL")
        for num in data[0].split():
            typ, data = box.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])

            pmail = mailparser.parse_from_bytes(data[0][1])
            print(f"От кого: {' '.join(pmail.from_[0])}")
            print(f"Тема: {pmail.subject}")
            print(f"Текст сообщения:\n{pmail.text_plain}")
            print('Файлы:', ' '.join([attfile['filename'] for attfile in pmail.attachments]))

            pmail.write_attachments('IMAP/attachments')

            t = datetime.now().strftime("%m-%y-%d=%H-%M-%S")
            filename = f'IMAP/{num}_{t}.txt'
            # print(filename)
            file = open(filename, 'w')
            file.write('')
            file.close()
            file = open(filename, 'a')
            file.write(f"От кого: {' '.join(pmail.from_[0])}\n")
            file.write(f"Тема: {pmail.subject}\n")
            file.write(f"Текст сообщения:\n{pmail.text_plain}\n")
            file.write('Файлы:'+ ' '.join([attfile['filename'] for attfile in pmail.attachments]))
            file.close()

            print()
    elif operation == '5':
        server = 'imap.gmail.com'
        port = '993'
        user = 'trisistest11@gmail.com'
        password = 'qwerty123_'
        box = imaplib.IMAP4_SSL(server, port)
        box.login(user, password)
        lst = box.list()
        box.select("inbox")
        result, data = box.search(None, "ALL")
        for num in data[0].split():
            typ, data = box.fetch(num, "(RFC822)")
            

            msg = email.message_from_bytes(data[0][1])
            pmail = mailparser.parse_from_bytes(data[0][1])
            print(f"От кого: {' '.join(pmail.from_[0])}")
            print(f"Тема: {pmail.subject}")
            print(f"Текст сообщения:\n{pmail.text_plain}")
            print('Файлы:', ' '.join([attfile['filename'] for attfile in pmail.attachments]))
            print()
            pmail.write_attachments('IMAP/attachments')

    elif operation == '0':
        print("goodbye")
        break
    else:
        print("Выберите из предложенного списка команд!")
    print("")
