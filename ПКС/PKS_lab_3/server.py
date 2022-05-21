import socket
DGRAM_SIZE = 20
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 51000))
while True:
    msg, addr = s.recvfrom(DGRAM_SIZE)
    msg = msg.decode()
    print('Client {} send: {}\n'.format(addr,msg))
    s.sendto(msg.encode(), addr)
