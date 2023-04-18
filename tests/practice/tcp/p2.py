import socket

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the remote peer
host = 'localhost'
port = 8000
sock.connect((host, port))
print(f"Connected to {host}:{port}")

# send a message to the peer
message = 'Hello, peer!'
sock.sendall(message.encode())

# receive a message from the peer
data = sock.recv(1024)
print('Received message:', data.decode())

# close the socket
sock.close()