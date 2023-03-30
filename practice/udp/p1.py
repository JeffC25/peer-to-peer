import socket

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a specific port and address
host = 'localhost'
port = 8000
sock.bind((host, port))

# wait for a message from a peer
print('Waiting for a message...')
data, addr = sock.recvfrom(1024)
print('Received message:', data.decode())

# close the socket
sock.close()