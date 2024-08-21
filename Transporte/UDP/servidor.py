import socket

server_address = ('localhost', 12345)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)

print("Servidor UDP está pronto para receber mensagens...")

while True:
    message, client_address = server_socket.recvfrom(1024)
    print(f"Mensagem recebida de {client_address}: {message.decode()}")
    response = "Mensagem recebida"
    server_socket.sendto(response.encode(), client_address)