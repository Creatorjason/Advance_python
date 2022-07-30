import socket


HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
client.send('Hello World'.encode('utf-8'))
print(client.recv(1024).decode())
