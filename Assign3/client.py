import socket
import sys

# Check for correct command-line arguments
if len(sys.argv) != 3:
    print("Usage: python client.py <server_ip> <server_port>")
    sys.exit(1)

# Parse command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a socket object
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
clientSocket.connect((serverIP, serverPort))
print(f"Connected to server {serverIP}:{serverPort}")

while True:
    # Get a message from the user
    userMSG = input("Client: ")

    # Check if the user wants to exit
    if userMSG.lower() == "exit":
        clientSocket.send("exit".encode('utf-8'))
        print("Exiting the chat.")
        break

    # Send the user's message to the server
    clientSocket.send(userMSG.encode('utf-8'))

    # Receive and print the server's reply
    serverMSG = clientSocket.recv(1024).decode('utf-8')
    print(f"Server: {serverMSG}")

# Close the socket
clientSocket.close()