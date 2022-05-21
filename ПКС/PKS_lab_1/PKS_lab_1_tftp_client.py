import tftpy

client = tftpy.TftpClient(host='127.0.0.1')


while True:
    print("Соединение установлено, выберите команду:")
    print("0. Выход")
    print("1. Загрузить файл на сервер")
    print("2. Скачать файл с сервера")
    operation = input("Команда: ")
    if operation == '1':
        try:
            localFileName = input(
                "Введите имя загружаемого файла в локальной папке: ")
            servFileName = input(
                "Введите имя файла, которое он будет иметь на сервере: ")
            client.upload(filename=servFileName, input=localFileName)
        except Exception as ex:
            print(str(ex))

    elif operation == '2':
        try:
            servFileName = input("Введите имя файла на сервере: ")
            localFileName = input(
                "Введите имя файла, которое он бует иметь в локальной папке: ")
            client.download(filename=servFileName, output=localFileName)

        except:
            print("Ошибка при скачивании файла с сервера")

    elif operation == '0':
        print("goodbye")
        break
