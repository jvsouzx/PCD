import numpy as np
import matplotlib.pyplot as plt
from scipy.sinal import butter, lfilter

# Configurações iniciais
taxa_amostagem = 2500  # Taxa de amostragem em Hz
t = np.linspace(0, 1, taxa_amostagem)  # Vetor de tempo para 1 segundo

# Função para gerar sinais senoidais
def gera_sinal(freq, amplitude=1.0):
    return amplitude * np.sin(2 * np.pi * freq * t)

# Geração dos sinais de entrada
sinal1 = gera_sinal(50, amplitude=1.0)   # Sinal de 50 Hz
sinal2 = gera_sinal(100, amplitude=0.8)  # Sinal de 100 Hz
sinal3 = gera_sinal(200, amplitude=0.6)  # Sinal de 200 Hz

# Multiplexação: soma dos sinais
sinal_multiplexado = sinal1 + sinal2 + sinal3

# Função para aplicar filtro passa-faixa
def filtro_passa_faixa(data, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y

# Demultiplexação: Aplicar filtros passa-faixa
demux_sinal1 = filtro_passa_faixa(sinal_multiplexado, 45, 55, taxa_amostagem)
demux_sinal2 = filtro_passa_faixa(sinal_multiplexado, 95, 105, taxa_amostagem)
demux_sinal3 = filtro_passa_faixa(sinal_multiplexado, 195, 205, taxa_amostagem)

# Visualização
plt.figure(figsize=(12, 10))

# Sinais de entrada
plt.subplot(4, 1, 1)
plt.title("Sinais de Entrada")
plt.plot(t, sinal1, label="50 Hz")
plt.plot(t, sinal2, label="100 Hz")
plt.plot(t, sinal3, label="200 Hz")
plt.legend()

# Sinal Multiplexado
plt.subplot(4, 1, 2)
plt.title("Sinal Multiplexado")
plt.plot(t, sinal_multiplexado, color='orange')

# Sinais Demultiplexados
plt.subplot(4, 1, 3)
plt.title("Sinais Demultiplexados")
plt.plot(t, demux_sinal1, label="50 Hz Demultiplexado")
plt.plot(t, demux_sinal2, label="100 Hz Demultiplexado")
plt.plot(t, demux_sinal3, label="200 Hz Demultiplexado")
plt.legend()

plt.tight_layout()
plt.show()
