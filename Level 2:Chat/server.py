import socket
s = socket.socket()
s.bind(('localhost', 5050))
s.listen(3)
print('Server is waiting for connection...')
c, addr = s.accept()
print("Connected with", addr)
while True:

    message = c.recv(1024).decode('utf-8')

    if not message:
        print("Client disconnected")
        break

    print(f"Received from client: {message}")

    if message.lower() == "exit":
        print("Client requested to exit")
        c.send("Goodbye!".encode('utf-8'))
        break

    c.send(message.encode('utf-8'))
    print(f"Echoed back: {message}")

c.close()
s.close()
print("Connection closed. Server terminated.")
