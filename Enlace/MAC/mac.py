import random
import time

class Device:
    def __init__(self, name):
        self.name = name
        self.data_to_send = random.randint(1, 5)  # Cada dispositivo tem de 1 a 5 pacotes para enviar.

    def attempt_transmission(self, medium):
        if medium.is_busy:
            print(f"{self.name}: Meio ocupado. Tentando novamente mais tarde.")
            return False
        else:
            print(f"{self.name}: Meio livre. Transmitindo {self.data_to_send} pacotes.")
            medium.is_busy = True
            time.sleep(random.uniform(0.1, 0.5))  # Simula o tempo de transmissão.
            medium.is_busy = False
            return True

class TransmissionMedium:
    def __init__(self):
        self.is_busy = False

def simulate_aloha(devices, medium):
    while any(device.data_to_send > 0 for device in devices):
        for device in devices:
            if device.data_to_send > 0:
                if device.attempt_transmission(medium):
                    device.data_to_send -= 1
                else:
                    collision_time = random.uniform(0.1, 0.5)  # Tempo de espera aleatório em caso de colisão.
                    print(f"{device.name}: Colisão detectada. Esperando {collision_time:.2f} segundos.")
                    time.sleep(collision_time)

def main():
    # Criando os dispositivos.
    devices = [Device(f"Dispositivo {i+1}") for i in range(4)]

    # Criando o meio de transmissão compartilhado.
    medium = TransmissionMedium()

    # Iniciando a simulação.
    simulate_aloha(devices, medium)

    print("Transmissão concluída.")

if __name__ == "__main__":
    main()
