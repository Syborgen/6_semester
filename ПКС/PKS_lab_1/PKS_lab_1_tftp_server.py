import tftpy
server = tftpy.TftpServer(tftproot='tftpboot')
server.listen(listenip='127.0.0.1')
