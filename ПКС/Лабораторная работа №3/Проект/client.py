import socket

DGRAM_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

out_str = input('-> ')
while out_str != 'end':
    s.sendto(out_str.encode(), ('localhost', 51000))
    in_str, addr = s.recvfrom(DGRAM_SIZE)
    print(f'Server answer: {in_str.decode()}')
    out_str = input('-> ')
