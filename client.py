multicasting with threads 

import socket
import threading

# Function to send and receive messages
def send_receive(client_socket):
    while True:
        message = input(" -> ")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        if message.lower().strip() == 'bye':
            break

# Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('10.11.149.35', 12345))  # Replace 'server_ip_address' with the server's IP and 12345 with the server's port

# Start a separate thread for sending and receiving messages
thread = threading.Thread(target=send_receive, args=(client_socket,))
thread.start()
