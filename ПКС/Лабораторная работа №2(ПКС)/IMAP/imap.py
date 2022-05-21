import imaplib
import mailparser
import getpass
import sys

if __name__ == '__main__':
    connect = imaplib.IMAP4_SSL('imap.gmail.com')
    login = input('email: ')
    password = getpass.getpass('password: ')
    if not login and not password:
        login = 'silurcpppy@gmail.com'
        password = 'smtplib1'

    try:
        print(f"connect: {connect.login(login, password)[1][0].decode()}")
    except BaseException:
        print('Wrong login or password.')
        sys.exit(-1)

    result, boxes = connect.list()
    print(f'a result of list: {result}')
    for box in boxes:
        print(box.decode('utf-8'))
    print(f"Select INBOX: {connect.select('INBOX')}")
    result, data = connect.uid('search', None, 'ALL')
    print(f"a result of search: {result} uids: ", data)
    uids = data[0].split()[-1:-11:-1]
    print(f'uids = {uids}\n')

    for i in uids:
        result, data = connect.uid('fetch', i, '(RFC822)')
        print(f'Message: {str(i)}')
        parse = mailparser.parse_from_bytes(data[0][1])
        print(f"From: {' '.join(parse.from_[0])}")
        print(f"To: {parse.delivered_to}")
        print(f"Subject: {parse.subject}")
        print(f'Дата: {parse.date.replace(hour=parse.date.hour + 3)}')
        print('Text:\n' + ''.join(parse.text_plain))
        print('Files:\n', ' '.join([file['filename'] for file in parse.attachments]))
        print('-' * 30, '\n')
        parse.write_attachments('imap_attachments')