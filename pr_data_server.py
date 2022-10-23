"""Server receives messages from clients and sends responses"""

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from select import select

with socket(AF_INET, SOCK_STREAM) as server_cock:
    server_cock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_cock.bind(('', 8007))
    server_cock.listen(1)
    server_cock.settimeout(1) # allow accept() wait only 1 sec
    client_sockets = []

    while True:
        try:
            client_sock, address = server_cock.accept()
        except OSError as e:
            print(e.errno)
        else:
            client_sockets.append(client_sock)
        finally:
            for client_socket in client_sockets:
                cl_read = []
                cl_read, cl_write, _ = select(client_sockets, client_sockets, [], 0)
                if client_socket in cl_read: # recieve() not block flow when no msg
                    data = client_socket.recv(4096)
                    print(f"Message: {data.decode('utf-8')} was sent by the client {address})")
                for client_socket in cl_write:
                    MSG = data.decode('utf-8')
                    print(MSG)
                    client_socket.send(MSG.encode('utf-8'))

