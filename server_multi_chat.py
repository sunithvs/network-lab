import socket

HOST ='127.0.0.1:8000'
PORT=65123
clients={}
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen(2)
	conn,addr = s.accept()
	print("adddress",addr)
	with conn:
		while True:
			data=conn.recv(1024)
			if data==b'connect':
				print("connection request from",addr)
				clients[addr[0]+":"+str(addr[1])]=conn
				print(clients)
			print(data)
print("server stoped")
