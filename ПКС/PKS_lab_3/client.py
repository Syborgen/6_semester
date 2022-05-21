import socket
D_SIZE = 10
DGRAM_SIZE = 20
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
out_str = input('Your message: ')
l = len(out_str)
a = 0
while out_str != 'exit':
	print(l)
	while(l>D_SIZE):
		s.sendto(out_str[a:a+D_SIZE].encode(), ('localhost', 51000))
		in_str, addr = s.recvfrom(DGRAM_SIZE)
		print('Server answer: {}'.format(in_str.decode()))
		l-=D_SIZE
		a+=D_SIZE
	s.sendto(out_str[a:len(out_str)].encode(), ('localhost', 51000))
	in_str, addr = s.recvfrom(DGRAM_SIZE)
	print('Server answer: {}'.format(in_str.decode()))
	out_str = input('Your message: ')
	l=len(out_str)
	a=0
