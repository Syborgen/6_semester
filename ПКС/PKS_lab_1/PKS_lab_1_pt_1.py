import ftplib

host = input("host: ")
if host == '':
	host = '127.0.0.1'
ftp_user = input("user: ")
if ftp_user == '':
	ftp_user = 'admin'
ftp_password = input("password: ")

try:
	try:
		ftp = ftplib.FTP(host, ftp_user,ftp_password)
	except:
			print("Ошибка авторизации")
	while True:
		print("Соединение установлено, выберите команду:")
		print("0. Выход")
		print("1. Вывести содержимое текущего каталога")
		print("2. Создать каталог")
		print("3. Удалить каталог")
		print("4. Удалить файл")
		print("5. Загрузить файл на сервер")
		print("6. Скачать файл с сервера")
		print("7. Перейти к другому каталогу")

		operation=input("(Текущая папка:"+ftp.pwd()+" ) Команда: ")
		if operation=='1':
			print(ftp.dir())

		elif operation == '2':
			try:
				ftp.mkd(input("Имя папки: "))
			except:
				print("Ошибка при создании папки")

		elif operation == '3':
			try:
				ftp.rmd(input("Имя папки: "))
			except:
				print("Ошибка при удалении папки")

		elif operation == '4':
			try:
				ftp.delete(input("Имя файла: "))
			except:
				print("Ошибка при удалении файла")



		elif operation == '5':
			try:
				upload = input("Имя файла: ")
				ftp.storbinary("STOR "+upload, open(upload, 'rb'))
			except:
				print("Ошибка при загрузке файла c сервеа")

		elif operation == '6':
			try:
				download = input("Имя файла: ")
				ftp.retrbinary("RETR "+download, open(download, 'wb').write)
			except:
				print("Ошибка при загрузке файла c сервеа")

		elif operation == '7':
			try:
				ftp.cwd(input("Куда перейти: "))
			except:
				print("Ошибка при изменении текущей директории")

		elif operation == '0':
			print("goodbye")
			ftp.quit()
			break
		else:
			print("Выберите из предложенного списка команд!")
		print("")
except:
	print('Ошибка сервера')

