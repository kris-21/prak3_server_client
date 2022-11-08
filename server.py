import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',3000))
server.listen(6)
print('Соединение устанавливается...')
client_socket, address = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print('Соединение установлено.', address[0],':',address[1])
print(data)
answer = 'Добро пожаловать!'
content = answer.encode('utf-8')
client_socket.send(content)
print('Соединение прервано.')