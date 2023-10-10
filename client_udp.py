import socket

HOST ='127.0.0.1'
PORT=65433

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.connect((HOST,PORT))
while True:
	text = input("Enter text to send to server")
	s.sendall(bytes(text, 'utf-8'))
	data = s.recv(1024)
	print("Received data",data)
