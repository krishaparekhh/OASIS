import socket
import threading

# Define the server host and port
host = '127.0.0.1'
port = 12345

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(2)
print(f"Server is listening on {host}:{port}...")

clients = []

# Handle incoming messages from clients
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message.lower() == 'exit':
                print(f"Connection from {client_address} closed")
                client_socket.close()
                clients.remove(client_socket)
                break
            print(f"Message from {client_address}: {message}")
            broadcast_message(message, client_socket)
        except:
            break

# Broadcast message to all clients
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# Accept new connections
def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

accept_connections()
