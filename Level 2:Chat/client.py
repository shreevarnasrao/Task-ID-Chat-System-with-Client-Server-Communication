import socket
c = socket.socket()

c.connect(('localhost', 5050))
print("Connected to server")
print("Type 'exit' to disconnect\n")
while True:

    message = input("You: ")

    c.send(message.encode('utf-8'))

    response = c.recv(1024).decode('utf-8')
    print(f"Server: {response}")

    if message.lower() == "exit":
        print("Disconnected from server")
        break

c.close()
print("Connection closed. Client terminated.")
