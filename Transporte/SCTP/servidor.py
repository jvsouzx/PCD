import sctp
import socket

server_address = ('localhost', 12345)
server_socket = sctp.sctpsocket_tcp(socket.AF_INET)
server_socket.bind(server_address)
server_socket.listen(5)

print("Servidor SCTP [OK!]...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Associação estabelecida com {client_address}")

    message = client_socket.recv(1024).decode()
    print(f"Mensagem recebida: {message}")
    response = "Mensagem recebida!"
    client_socket.send(response.encode())

    client_socket.close()