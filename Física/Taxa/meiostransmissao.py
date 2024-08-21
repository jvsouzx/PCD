import random
import matplotlib.pyplot as plt

# Define as taxas de transmissão médias em Mbps (Megabits por segundo) para cada meio de transmissão
taxas_transmissao = {
    "par_trancado": 100,      # Taxa média de um cabo de par trançado Cat5e/Cat6
    "coaxial": 50,            # Taxa média de um cabo coaxial moderno
    "fibra_optica": 1000      # Taxa média de um cabo de fibra óptica multimodo
}

# Define os possíveis meios de transmissão
meios = ["par_trancado", "coaxial", "fibra_optica"]

# Função para simular a taxa de transmissão
def simular_taxa_transmissao(meio, tempo_segundos):
    # Obtém a taxa de transmissão para o meio especificado
    taxa_mbps = taxas_transmissao.get(meio, 0)

    # Introduz uma variação aleatória para simular a instabilidade na taxa de transmissão
    variacao = random.uniform(-0.1, 0.1)  # Variação de até ±10%

    # Calcula a taxa de transmissão ajustada
    taxa_ajustada = taxa_mbps * (1 + variacao)
    
    # Calcula o total de dados transmitidos durante o tempo especificado
    total_dados = taxa_ajustada * tempo_segundos
    return total_dados

# Parâmetros da simulação
tempo_simulacao = 120  # Tempo de simulação em segundos

# Lista para armazenar os dados transmitidos por cada meio
dados_transmitidos_lista = []

# Simula e armazena a transmissão para cada meio
for meio in meios:
    dados_transmitidos = simular_taxa_transmissao(meio, tempo_simulacao)
    dados_transmitidos_lista.append(dados_transmitidos)
    print(f"Meio: {meio.replace('_', ' ').title()} - Dados transmitidos em {tempo_simulacao} segundos: {dados_transmitidos:.2f} Megabits")

# Cria o gráfico comparativo
plt.figure(figsize=(10, 6))
plt.bar([meio.replace('_', ' ').title() for meio in meios], dados_transmitidos_lista, color=['blue', 'orange', 'green'])

# Adiciona título e labels
plt.title("Comparação de Dados Transmitidos em Diferentes Meios (10 segundos)")
plt.xlabel("Meios de Transmissão")
plt.ylabel("Dados Transmitidos (Megabits)")

# Exibe o gráfico
plt.show()
