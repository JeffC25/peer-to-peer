import socket
import database

class Peer():
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.address = self.sock.getsockname()

        self.host = "localhost"
        self.reciever = None

        sock.bind((self.host, 0))

    def displayAddress(self):
        print(f"Host: {self.sock.getsockname()[0]}")
        print(f"Ports: {self.sock.getsockname()[1]}")
    
    def connect(self, host, port):
        self.sock.connect((host, port))
        self.reciever = (host, port)
        print(f"Connected to {self.reciever}")
        return host, port

    def listen(self):
        self.sock.listen(1)
        print('Waiting for a connection...')
        connection, clientAddress = self.sock.accept()
        print(f"Connected to {clientAddress}")
        return connection, clientAddress

    def sendMessage(self, message):
        self.sock.sendall(message.encode())
        database.addMessage(str(self.address), str(self.reciever), message)

    def recieveMessage(self, connection, address):
        data = connection.recv(1024)
        print(f"Message from {address}:", data.decode())

    def close(self):
        self.sock.close()

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
        host = input("Host: ")
        port = int(input("Port: "))
        peer.connect(host, port)
        
        message = input("Enter message: ")
        peer.sendMessage(message)

    else:
        connection, address = peer.listen()
        peer.recieveMessage(connection, address)

if __name__ == '__main__':
    main()