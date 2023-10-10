import socket

HOST ='127.0.0.1'
PORT=10014

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(1)
print("kooi")
conn,addr = s.accept()

print('connnected to',addr)
while True:
	data=conn.recv(1024)
	print(data)
	if not data:
		break
	text=input("Enter the reply:")
	print(text)
	conn.sendall(bytes(text, 'utf-8'))
conn.close()
