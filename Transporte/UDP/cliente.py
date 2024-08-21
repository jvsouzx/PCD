import socket

server_address = ('localhost', 12345)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Digite a mensagem a ser enviada para o servidor: ")
client_socket.sendto(message.encode(), server_address)

response, server = client_socket.recvfrom(1024)
print(f"Resposta do servidor: {response.decode()}")

client_socket.close()