import socket

# Define the server IP address and port
serverIP = "127.0.0.1"  # Server's IP address
serverPort = 12345  # Choose a port number

# Create a socket object
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server IP and port
serverSocket.bind((serverIP, serverPort))

# Listen for incoming connections (maximum 1 client in this example)
serverSocket.listen(1)
print(f"Server is listening on {serverIP}:{serverPort}")

# Accept a client connection
clientSocket, clientAddress = serverSocket.accept()
print(f"Accepted connection from {clientAddress}")

while True:
    # Receive data from the client
    clientMSG = clientSocket.recv(1024).decode('utf-8')

    # Check if the client wants to exit
    if clientMSG.lower() == "exit":
        print("Client has requested to exit the chat.")
        break

    # Print the received message
    print(f"Client: {clientMSG}")

    # Get a message from the server user and send it to the client
    serverMSG = input("Server: ")
    clientSocket.send(serverMSG.encode('utf-8'))

# Close the sockets
clientSocket.close()
serverSocket.close()