import socket
import threading

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço de loopback (localhost)
PORT = 8080         # Porta do servidor

# Cria o socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor web rodando em http://{HOST}:{PORT}")

# Função para tratar cada requisição
def handle_request(client_socket):
    try:
        # Recebe a requisição do cliente
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Requisição recebida:\n{request}")

        # Extrai o método e o caminho do recurso solicitado
        method, path, _ = request.split(' ')[0:3]
        print(f"Método: {method}, Recurso: {path}")

        # Responde com uma página HTML diferente dependendo do recurso solicitado
        if path == '/':
            response_body = "<html><body><h1>Home Page</h1><form action='/submit' method='post'><input type='text' name='name'><input type='submit' value='Enviar'></form></body></html>"
            status_line = "HTTP/1.1 200 OK\r\n"
        elif path == '/about':
            response_body = "<html><body><h1>About Page</h1></body></html>"
            status_line = "HTTP/1.1 200 OK\r\n"
        elif method == 'POST' and path == '/submit':
            content_length = int(request.split('Content-Length: ')[1].split('\r\n')[0])
            body = client_socket.recv(content_length).decode('utf-8')
            print(f"Dados recebidos: {body}")

            response_body = "<html><body><h1>Formulário Recebido</h1></body></html>"
            status_line = "HTTP/1.1 200 OK\r\n"
        else:
            response_body = "<html><body><h1>404 Not Found</h1></body></html>"
            status_line = "HTTP/1.1 404 Not Found\r\n"

        # Monta a resposta HTTP
        response_headers = "Content-Type: text/html\r\n"
        response = status_line + response_headers + "\r\n" + response_body

        # Envia a resposta ao cliente
        client_socket.sendall(response.encode('utf-8'))
    except Exception as e:
        print(f"Erro ao processar requisição: {e}")
    finally:
        # Fecha a conexão com o cliente
        client_socket.close()

# Loop principal para aceitar conexões
while True:
    client_conn, client_addr = server_socket.accept()
    print(f"Conexão estabelecida com {client_addr}")
    # Cria uma nova thread para tratar a requisição
    threading.Thread(target=handle_request, args=(client_conn,)).start()
