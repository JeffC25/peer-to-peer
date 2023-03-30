import asyncio
import socket

# create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a port and address
host = 'localhost'
sock.bind((host, 0))

print(f"Host: {sock.getsockname()[0]}")
print(f"Socket: {sock.getsockname()[1]}")

action = input("connect or wait: ")
while not (action == "connect" or action == "wait"):
    action = input("connect or wait: ")

if action == "connect":
    print("Connecting")
    connectHost = input("Host: ")
    connectPort = int(input("Port: "))
    sock.connect((connectHost, connectPort))
    print(f"Connected to {connectHost}:{connectPort}")

    message = input("Enter message: ")
    sock.sendall(message.encode())

else:
    sock.listen(1)
    print('Waiting for a connection...')
    connection, clientAddress = sock.accept()
    print(f"Connected to {clientAddress}")

    data = connection.recv(1024)
    print(f"Message from {clientAddress}:", data.decode())

sock.close()