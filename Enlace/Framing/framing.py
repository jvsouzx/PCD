import zlib
import random
import binascii

# Função para criar um quadro
def criar_quadro(dados):
    # Cabeçalho fictício
    cabecalho = {
        'endereco_origem': '192.168.1.1',
        'endereco_destino': '192.168.1.2',
        'numero_quadro': random.randint(1, 1000)
    }
    
    # Dados a serem transmitidos
    dados_bytes = dados.encode('utf-8')
    
    # Calcular CRC
    crc = zlib.crc32(dados_bytes)
    
    # Criar quadro (cabeçalho + dados + CRC)
    quadro = {
        'cabecalho': cabecalho,
        'dados': dados,
        'crc': crc
    }
    
    return quadro

# Função para transmitir um quadro
def transmitir_quadro(quadro):
    # Simular a transmissão com uma chance de erro
    erro = random.choice([True, False])
    if erro:
        # Introduzir um erro aleatório nos dados
        quadro['dados'] = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=len(quadro['dados'])))
        quadro['crc'] = zlib.crc32(quadro['dados'].encode('utf-8'))
    
    return quadro

# Função para verificar a integridade do quadro
def verificar_quadro(quadro):
    dados_bytes = quadro['dados'].encode('utf-8')
    crc_calculado = zlib.crc32(dados_bytes)
    return crc_calculado == quadro['crc']

# Exemplo de uso
dados = "Mensagem de teste"
quadro = criar_quadro(dados)
print("Quadro Criado:")
print(quadro)

quadro_transmitido = transmitir_quadro(quadro)
print("\nQuadro Transmitido:")
print(quadro_transmitido)

# Verificar a integridade do quadro recebido
if verificar_quadro(quadro_transmitido):
    print("\nQuadro recebido corretamente!")
else:
    print("\nErro na transmissão do quadro!")
