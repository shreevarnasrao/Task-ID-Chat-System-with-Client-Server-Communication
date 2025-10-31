import socket
s = socket.socket()
s.bind(('localhost', 5050))
s.listen(3)
print('waiting for connection')

c, addr = s.accept()
print("connected with", addr)

message = c.recv(1024).decode('utf-8')
print(f"Received from client: {message}")

c.send(message.encode('utf-8'))
print(f"Echoed back: {message}")

c.close()
s.close()
print("Connection closed. Server terminated.")
