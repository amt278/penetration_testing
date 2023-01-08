import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#mmkn tktb el ip bta3 el device bta3k (laz str)
hostname = socket.gethostname()
#port lazm ybaa >= 1024
port = 1024

server_socket.bind((hostname, port))
#lazm el server y3ml listen abl ma el client y3ml connect
server_socket.listen(3)
print('listening...')

while True:
    client_socket, address = server_socket.accept()

    print(f'receive connection from {str(address)}')
    msg = 'connected to server!'
    client_socket.send(msg.encode('ascii'))

    client_socket.close()
    if input() == 'q':
        break