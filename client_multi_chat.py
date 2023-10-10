import socket

HOST ='127.0.0.1'
PORT=1243

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))
s.sendall(b"connect")

while True:
	recv = input("Enter recv")
	if recv=="exit":
		break
	while True:
		
		msg = input("msg to send  :--> ")
		if msg=="close":
			s.sendall(bytes("close", 'utf-8'))
			break
		if msg:
			text=recv+":"+msg
			s.sendall(bytes(text, 'utf-8'))
		data = s.recv(1024)
		if data:
			print(recv,":--> ",data)
print("client is closing")
s.close()
