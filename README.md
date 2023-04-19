# Peer-to-peer

## Installation

#### Clone the repository in your machine
Enter the following command after opening command prompt
```batch
git clone https://github.com/JeffC25/peer-to-peer.git
```
#### Navigate to the directory containing the code
Replace &lt;path&gt; with the path of cloned directory
```batch
cd <path>
```
#### Run the following command to start the peer-to-peer network
You need to have [Python](https://www.python.org/downloads/) installed to run this
```batch
python p2p.py
```


## Documentation
#### This [Python code](./src/p2p.py) creates a simple peer-to-peer network using the [socket module](https://docs.python.org/3/library/socket.html) which allows the user to exchange messages.

#### It prompts the user to either connect to another peer or wait for another peer to connect. If the user chooses to connect, they are prompted for the host and port number of the peer they want to connect to. They can then enter a message to send to the connected peer. If the user chooses to wait, the program waits for another peer to connect and displays any received messages.


#### The Peer class has the following methods:

- `__init__()`: Initializes a new instance of the Peer class. It creates a new socket object and binds it to a host and port number.

- `displayAddress()`: Displays the host and port number that the socket is bound to.

- `connect(host, port)`: Connects to another peer with the specified host and port number.

- `listen()`: Waits for another peer to connect to the socket.

- `sendMessage(message)`: Sends a message to the connected peer.

- `receiveMessage(connection, address)`: Receives a message from the connected peer.

- `connOrWait()`: Helper function that prompts the user to either connect to another peer or wait for another peer to connect.

- `close()`: Helper function that closes the socket connection
