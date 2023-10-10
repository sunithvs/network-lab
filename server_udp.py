import socket

HOST ='127.0.0.1'
PORT=65433

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((HOST,PORT))


while True:
	data,addr=s.recvfrom(1024)
	print(data,addr)
	if not data:
		break
	s.sendto(b"pong",addr)

