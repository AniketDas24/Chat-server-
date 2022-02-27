import socket

HEADER_SIZE = 10
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = '127.0.0.1'
PORT = 1234

client_socket.connect((IP, PORT))

client_socket.setblocking(False)

# def transform_message(username, message):
#     full_message = f'len(username):<{HEADER_SIZE}'+'username'+f'len(message):<{HEADER_SIZE}'+'message'
#     return full_message
    
# def recive_message(client_socket):
#     username_header = client_socket.recv(HEADER_SIZE)
#     username_length = len(username_header.decode('utf-8'))
#     username = client_socket.recv(username_length).decode('utf-8')
    
#     message_header = client_socket.recv(HEADER_SIZE)
#     message_length = len(message_header.decode('utf-8'))
#     message = client_socket.recv(message_length).decode('utf-8')
    
#     return username, message

username = input('Username: ').encode('utf-8')
username_header = f'{len(username):<{HEADER_SIZE}}'.encode('utf-8')

client_socket.send(username_header + username)

while True:
    message = input(f'{username} > ')
    message_header = f'{len(message):<{HEADER_SIZE}}'.encode('utf-8')
    client_socket.send(message_header + message.encode('utf-8'))
    
    while True:
        username_header = client_socket.recv(HEADER_SIZE)
        username_length = int(username_header.decode('utf-8').strip())
        username = client_socket.recv(username_length).decode('utf-8')
        
        message_header = client_socket.recv(HEADER_SIZE)
        message_length = int(message_header.decode('utf-8').strip())
        message = client_socket.recv(message_length).decode('utf-8')
        print(f'{username} > {message}')
    
    
