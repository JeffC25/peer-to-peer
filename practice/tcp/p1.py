import socket

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific port and address
host = 'localhost'
port = 8000
sock.bind((host, port))

# listen for incoming connections
sock.listen(1)
print('Waiting for a connection...')

# accept an incoming connection
connection, client_address = sock.accept()
print(f"Connected to {client_address}")

# receive a message from the peer
data = connection.recv(1024)
print('Received message:', data.decode())

# send a message to the peer
message = 'Hello, peer!'
connection.sendall(message.encode())

# close the connection and socket
connection.close()
sock.close()