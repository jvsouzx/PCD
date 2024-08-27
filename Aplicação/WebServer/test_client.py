import socket

# Função para enviar requisição HTTP e receber a resposta
def send_request(method, path, body=None):
    # Configuração do servidor (deve coincidir com o servidor implementado)
    HOST = '127.0.0.1'
    PORT = 8080
    
    # Cria o socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    # Monta a requisição HTTP
    request_line = f"{method} {path} HTTP/1.1\r\n"
    headers = "Host: 127.0.0.1\r\n"
    if body:
        headers += f"Content-Length: {len(body)}\r\n"
        headers += "Content-Type: application/x-www-form-urlencoded\r\n"
    request = request_line + headers + "\r\n"
    if body:
        request += body
    
    # Envia a requisição ao servidor
    client_socket.sendall(request.encode('utf-8'))
    
    # Recebe a resposta do servidor
    response = client_socket.recv(4096)
    
    # Exibe a resposta
    print("Resposta do servidor:")
    print(response.decode('utf-8'))
    
    # Fecha a conexão
    client_socket.close()

# Teste da página principal (GET /)
print("=== Teste GET / ===")
send_request("GET", "/")

# Teste da página "About" (GET /about)
print("\n=== Teste GET /about ===")
send_request("GET", "/about")

# Teste da página inexistente (GET /notfound)
print("\n=== Teste GET /notfound ===")
send_request("GET", "/notfound")

# Teste do envio de formulário (POST /submit)
print("\n=== Teste POST /submit ===")
form_data = "name=TESTE"
send_request("POST", "/submit", form_data)
