import socket

HOST ='127.0.0.1'
PORT=65438

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))
while True:
	text = input("client :--> ")
	s.sendall(bytes(text, 'utf-8'))
	data = s.recv(1024)
	if data==b"close":
		s.sendall(bytes("close", 'utf-8'))
		break
	
	print("server: ",data)

print("client is closing")
s.close()
