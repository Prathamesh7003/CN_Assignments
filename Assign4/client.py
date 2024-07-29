import socket
import threading

# Function to receive and print messages from the server
def receiveMSG(clientSocket):
    while True:
        try:
            message = clientSocket.recv(1024).decode('utf-8')
            print(message)
        except:
            # Connection closed or lost
            break

# Function to send messages to the server
def sendMSG(clientSocket):
    while True:
        message = input()
        clientSocket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            break

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 7976))

# Get the user's name
name = input("Enter your name: ")
client.send(name.encode('utf-8'))

# Create threads for sending and receiving messages
receiveThread = threading.Thread(target=receiveMSG, args=(client,))
sendThread = threading.Thread(target=sendMSG, args=(client,))

# Start the threads
receiveThread.start()
sendThread.start()