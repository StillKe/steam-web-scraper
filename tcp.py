import socket

HOST = 'www.google.com'  # Server hostname or IP address
PORT = 80                # The standard port for HTTP is 80, for HTTPS it is 443

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
client_socket.connect(server_address)

request_header = b'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
client_socket.sendall(request_header)

response = b''  # Use bytes object instead of string for binary data
while True:
    recv = client_socket.recv(1024)
    if not recv:
        break
    response += recv

print(response.decode('utf-8'))  # Decode bytes to string using UTF-8
client_socket.close()
