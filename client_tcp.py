import socket

HOST = '127.0.0.1'
PORT = 10014

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))


while True:
	text = input("Enter text to send to server")
	if text=="close":
		break
	s.sendall(bytes(text, 'utf-8'))
	data = s.recv(1024)
	print("Received data",data)
s.close()
