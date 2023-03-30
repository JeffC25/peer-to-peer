import asyncio
import socket

# create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a port and address
host = 'localhost'
sock.bind((host, 0))

# display address info
print(f"Host: {sock.getsockname()[0]}")
print(f"Socket: {sock.getsockname()[1]}")

# ask user to wait or input address to connect to
action = input("connect or wait: ")
while not (action == "connect" or action == "wait"):
    action = input("connect or wait: ")

# connect to a host
if action == "connect":
    print("Connecting")
    connectHost = input("Host: ")
    connectPort = int(input("Port: "))
    sock.connect((connectHost, connectPort))
    print(f"Connected to {connectHost}:{connectPort}")

    # send message
    message = input("Enter message: ")
    sock.sendall(message.encode())

# wait for connection
else:
    sock.listen(1)
    print('Waiting for a connection...')
    connection, clientAddress = sock.accept()
    print(f"Connected to {clientAddress}")

    # recieve message
    data = connection.recv(1024)
    print(f"Message from {clientAddress}:", data.decode())

# close socket
sock.close()
