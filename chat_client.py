import socket
import threading

# Define the server host and port
host = '127.0.0.1'
port = 12345

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"New message: {message}")
        except:
            print("Error receiving message.")
            break

# Function to send messages to the server
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
        if message.lower() == 'exit':
            break

# Start the thread for receiving messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start sending messages
send_message()

client_socket.close()
