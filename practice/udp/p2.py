import socket

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to a specific port and address
host = 'localhost'
port = 8000

# send a message to the first peer
message = 'Hello, first peer!'
sock.sendto(message.encode(), (host, port))

# close the socket
sock.close()