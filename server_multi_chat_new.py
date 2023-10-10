import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '192.168.10.109'
port = 1247
ThreadCount = 0

clients={}
new_clients={}

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection,address):
	new_clients[address[1]]=connection
	while True:
		data = connection.recv(2048).decode()
		data=str(data)
		if data==b"connect":
			continue
		print(data)
		try:
			client,msg=data.split(":")
			if client=="name":
				clients[msg]=new_clients[address[1]]
			if  msg=="quit":
				break
			if client in clients:
				print("sending to",client)
				clients[client].sendall(str.encode(msg))
		except Exception as e:
			print("exp",e)
	connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    print("clients",clients)
    start_new_thread(threaded_client, (Client,address ))
    
ServerSocket.close()
