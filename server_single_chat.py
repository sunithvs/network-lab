import socket

HOST ='127.0.0.1'
PORT=65438

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print("server ready to accept connections")
conn,addr = s.accept()

with conn:
	while True:
		data=conn.recv(1024)
		print("client: ",data )
		if data==b"close":
			conn.sendall(bytes("close",'utf-8'))
			break
		text = input("server :-->")
		conn.sendall(bytes(text,'utf-8'))

print("server stoped")
