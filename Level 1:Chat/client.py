import socket

c = socket.socket()

c.connect(('localhost', 5050))

print(c.recv(1024))

message = input("Hello")
c.send(message.encode('utf-8'))
print(f"Sent: {message}")
response = c.recv(1024).decode('utf-8')
print(f"Received from server: {response}")

c.close()
print("Connection closed. Client terminated.")
