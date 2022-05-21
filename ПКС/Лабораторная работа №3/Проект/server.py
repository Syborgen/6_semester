import socket

DGRAM_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('localhost', 51000))

while True:
    msg, addr = s.recvfrom(DGRAM_SIZE)
    print(f'Client: {addr}')
    msg = msg.decode()
    print(f'Message:{msg}')
    s.sendto(msg.encode(), addr)
