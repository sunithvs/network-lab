import socket

HOST ='192.168.10.109'
PORT=1247

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((HOST,PORT))
s.sendall(b"connect")
recv = input("Enter your name")
text="name"+":"+recv.strip().lower()
s.sendall(bytes(text, 'utf-8'))

while True:
	
	recv = input("Enter sender'S name")
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
