import sctp
import socket

server_address = ('localhost', 12345)
client_socket = sctp.sctpsocket_tcp(socket.AF_INET)

client_socket.connect(server_address)

message = input("Digite a mensagem a ser enviada para o servidor: ")

client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f"Resposta do servidor: {response}")

client_socket.close()