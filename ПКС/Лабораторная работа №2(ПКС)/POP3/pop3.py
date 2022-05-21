import poplib
from getpass import getpass
import mailparser
import sys

if __name__ == '__main__':
    login = input('login: ')
    password = getpass('password: ')
    if not login and not password:
        login = 'silurcpppy@gmail.com'
        password = 'smtplib1'

    server = poplib.POP3_SSL('pop.gmail.com', 995)
    try:
        server.user(login)
        server.pass_(password)
    except BaseException:
        print("Wrong login or password.")
        sys.exit(-1)

    response, message_sizes, octets = server.list()
    message_count, _ = server.stat()
    print(f'Message count: {message_count}')
    for msgnum, msgsize in [i.decode().split() for i in message_sizes]:
        resp, lines, octets = server.retr(msgnum)
        msgtext = b"\n".join(lines) + b"\n\n"
        mail = mailparser.parse_from_bytes(msgtext)
        print(f"Message: {msgnum}")
        print(f"От: {' '.join(mail.from_[0])}")
        print(f'Кому: {mail.delivered_to}')
        print(f'Тема: {mail.subject}')
        print(f'Дата: {mail.date.replace(hour=mail.date.hour + 3)}')
        print("Сообщение:\n" + ''.join(mail.text_plain))
        print("Файлы:\n" + ' '.join([file['filename'] for file in mail.attachments]))
        mail.write_attachments('pop3_attachments')
        print('Отключение от сервера. Удаление сообщений.')
        server.quit()
        print('Выход...')
