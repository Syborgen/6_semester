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


msg = MIMEMultipart()
msg.encoding = 'quoted printable'
msg['Subject'] = Header('Тема')
msg['From'] = Header('kirill.danilchuk@gmail.com')
msg['To'] = Header('kirill.danilchuk123@gmail.com')
msg.attach(MIMEText('Привет, я текст.', 'plain', 'utf-8'))
attach_file('imap.py', msg)

with open('mime.txt', 'wt') as fd:
    fd.write(msg.as_string())
