import socket
import threading
import time

# Global variables to store connected clients and their names
clients = {}
addresses = {}

# Function to broadcast messages to all connected clients
def broadcast(MSG, clientSocket):
    for client in clients:
        if client != clientSocket:
            try:
                client.send(MSG)
            except:
                # Remove the client if unable to send a message
                remove(client)

# Function to handle incoming client connections
def handleClient(clientSocket):
    try:
        # Get the client's name
        name = clientSocket.recv(1024).decode('utf-8')
        welcomeMSG = f"Welcome, {name}! Type 'exit' to leave the chat room."
        clientSocket.send(welcomeMSG.encode('utf-8'))

        # Notify other clients about the new user
        MSG = f"{name} has joined the chat."
        broadcast(MSG.encode('utf-8'), clientSocket)

        # Store the client's information
        clients[clientSocket] = name

        while True:
            MSG = clientSocket.recv(1024)
            if MSG:
                # Broadcast the message to all clients
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                MSGtoBroadcast = f"[{timestamp}] {name}: {MSG.decode('utf-8')}"
                broadcast(MSGtoBroadcast.encode('utf-8'), clientSocket)
            else:
                # Remove the client if no message received
                remove(clientSocket)
                break
    except Exception as e:
        print(f"Error handling client: {str(e)}")

# Function to remove a client from the chat
def remove(clientSocket):
    if clientSocket in clients:
        name = clients[clientSocket]
        del clients[clientSocket]
        message = f"{name} has left the chat."
        broadcast(message.encode('utf-8'), clientSocket)
    clientSocket.close()

# Function to gracefully shut down the server
def shutdownServer():
    # Notify clients about the server shutting down
    shutdownMSG = "Server is shutting down."
    for clientSocket in clients:
        try:
            clientSocket.send(shutdownMSG.encode('utf-8'))
        except:
            pass
    # Close all client sockets and exit
    for clientSocket in clients:
        clientSocket.close()
    server.close()
    print("Server is shutting down.")
    exit()

# Function to listen for console input
def consoleListener():
    while True:
        command = input()
        if command == 'exit':
            shutdownServer()

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 7976))
server.listen(5)
print("Server is listening for incoming connections...")

# Start the console listener thread
consoleThread = threading.Thread(target=consoleListener)
consoleThread.start()

while True:
    try:
        clientSocket, clientAddress = server.accept()
        print(f"Accepted connection from {clientAddress[0]}:{clientAddress[1]}")
        
        # Create a thread to handle the client
        clientThread = threading.Thread(target=handleClient, args=(clientSocket,))
        clientThread.start()
    except Exception as e:
        print(f"Error accepting client connection: {str(e)}")
        break