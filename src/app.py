import socket
import database

class Peer():
    # instiantiate peer object and bind to socket
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.address = self.sock.getsockname()

        self.host = "localhost"
        self.reciever = None

        sock.bind((self.host, 0))

    # print host address to terminal
    def displayAddress(self):
        print(f"Host: {self.sock.getsockname()[0]}")
        print(f"Ports: {self.sock.getsockname()[1]}")
    
    # connect to peer
    def connect(self, host, port):
        self.sock.connect((host, port))
        self.reciever = (host, port)
        print(f"Connected to {self.reciever}")
        return host, port

    # listen for incoming connection from peer
    def listen(self):
        self.sock.listen(1)
        print('Waiting for a connection...')
        connection, clientAddress = self.sock.accept()
        print(f"Connected to {clientAddress}")
        return connection, clientAddress

    # send message to peer
    def sendMessage(self, message):
        self.sock.sendall(message.encode())
        database.addMessage(str(self.address), str(self.reciever), message)

    # recieve message from peer
    def recieveMessage(self, connection, address):
        data = connection.recv(1024)
        print(f"Message from {address}:", data.decode())

    # close connection
    def close(self):
        self.sock.close()

# prompt user to connect to peer or listen for connection
def connOrWait():
    action = input("Connect (c) or wait (w): ")
    while not (action == "c" or action == "w"):
        action = input("Connect (c) or wait (w): ")
    return action

def main():
    database.createDatabase()
    print("initializing")
    peer = Peer()
    peer.displayAddress()
    action = connOrWait()

    if action == 'c':
        # prompt user to input address to connect to
        host = input("Host: ")
        port = int(input("Port: "))

        # connect to peer
        peer.connect(host, port)
        
        # send message
        message = input("Enter message: ")
        peer.sendMessage(message)

    else:
        # listen to incoming connection
        connection, address = peer.listen()

        # recieve message
        peer.recieveMessage(connection, address)

if __name__ == '__main__':
    main()
