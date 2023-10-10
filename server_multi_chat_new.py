import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1243
ThreadCount = 0s

clients={}

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection,address):
	clients[address[1]]=connection
	while True:
		data = connection.recv(2048).decode()
		data=str(data)
		if data==b"connect":
			continue
		print(data)
		try:
			client,msg=data.split(":")
			if  msg=="quit":
				break
			if int(client) in clients:
				print("sending to",client)
				clients[int(client)].sendall(str.encode(msg))
		except Exception as e:
			print("exp",e)
	connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    print("clients",clients)
    start_new_thread(threaded_client, (Client,address ))
    
ServerSocket.close()
