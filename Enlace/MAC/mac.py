import random
import time
import threading

class Dispositivo(threading.Thread):
    def __init__(self, nome, canal):
        threading.Thread.__init__(self)
        self.nome = nome
        self.canal = canal

    def run(self):
        while True:
            # O dispositivo tenta transmitir dados
            if self.canal.ocupado:
                print(f'{self.nome}: O canal está ocupado, aguardando...')
                time.sleep(random.uniform(1, 3))  # Espera um tempo aleatório antes de tentar novamente
            else:
                print(f'{self.nome}: Tentando transmitir...')
                self.canal.ocupado = True  # O canal está agora ocupado
                time.sleep(random.uniform(0.5, 1.5))  # Tempo de transmissão

                # Verifica se houve colisão
                if self.canal.colisao_ocorreu():
                    print(f'{self.nome}: Colisão detectada! Aguardando para tentar novamente...')
                    time.sleep(random.uniform(1, 3))  # Espera um tempo aleatório antes de tentar novamente
                else:
                    print(f'{self.nome}: Transmissão bem-sucedida!')
                    self.canal.ocupado = False  # Libera o canal após a transmissão

class Canal:
    def __init__(self):
        self.ocupado = False
        self.transmissores = 0

    def colisao_ocorreu(self):
        return self.transmissores > 1

    def registrar_transmissao(self):
        self.transmissores += 1

    def finalizar_transmissao(self):
        self.transmissores -= 1

def simular_aloha():
    canal = Canal()
    dispositivos = [Dispositivo(f'Dispositivo-{i}', canal) for i in range(5)]  # 5 dispositivos na rede

    for dispositivo in dispositivos:
        dispositivo.start()

    for dispositivo in dispositivos:
        dispositivo.join()

if __name__ == "__main__":
    simular_aloha()