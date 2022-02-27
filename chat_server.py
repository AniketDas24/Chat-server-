import socket
import select

HEADER_SIZE =10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = '127.0.0.1'
PORT = 1234

server_socket.bind((IP, PORT))

socket_lst = [server_socket]
clients = {}

def recive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_SIZE)
        message_length = len(message_header.decode('utf-8'))
        message = client_socket.recv(message_length)
        return {'header':message_header, 'data':message}
    except:
        return False
    
server_socket.listen()

while True:
    read_sockets,_,exceptonnal_sockets = select.select(socket_lst, [], socket_lst)
    for notified_socket in read_sockets:
        if notified_socket==server_socket:
            client_socket, client_address = server_socket.accept()
            user = recive_message(client_socket)
            if user==False:
                continue
            socket_lst.append(client_socket)
            clients[client_socket] = user
            print(f"{user['data'].decode('utf-8')} has connected")            
        else:
            message = recive_message(notified_socket)
            user = clients[notified_socket]
            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            

        for client_socket in clients:
            if clients!=notified_socket:
                client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
            


