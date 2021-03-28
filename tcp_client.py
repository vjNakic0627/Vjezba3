 
# tcp_client.py
import socket
client_socket = socket.socket()
host = socket.gethostname()
port = 9999
 
client_socket.connect((host, port))
print('socket se uspješno spojio na Google na port = ',port,' i IP adresu = ' ,host)
 
client_socket.close()