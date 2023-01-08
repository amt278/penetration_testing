import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 1024

client_socket.connect((host, port))

msg = client_socket.recv(1024) #aktr haga mmkn yakhodha

client_socket.close()

print(msg.decode('ascii'))