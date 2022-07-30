import socket

HOST = "127.0.0.1" 



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
server.bind((HOST, 9999))
server.listen()
print('waiting for connections')

while True:
    client, addr = server.accept()
    print('Connected with', client)

    message = client.recv(1024).decode('utf-8')
    print('message')
    send_message = client.send("Got youe message".encode('utf-8'))

    client.close()
    print(f'connection with {addr} ended')
