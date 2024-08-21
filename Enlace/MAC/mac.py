import random
import time
import threading

# Parâmetros da simulação
NUM_DEVICES = 5
TRANSMISSION_TIME = 2  # Tempo necessário para transmitir dados
COLLISION_WAIT_TIME = 1  # Tempo para esperar após uma colisão

# Estado do meio de transmissão
transmitting = [False] * NUM_DEVICES  # Lista que indica se um dispositivo está transmitindo
lock = threading.Lock()  # Lock para garantir exclusão mútua ao acessar a lista de transmissão

def device_transmission(device_id):
    global transmitting

    while True:
        # Espera um tempo aleatório antes de tentar transmitir
        time.sleep(random.uniform(1, 3))
        
        with lock:
            # Verifica se o meio está livre
            if any(transmitting):
                print(f"Dispositivo {device_id} detectou que o meio está ocupado. Aguardando...")
                return
        
            # Começa a transmitir
            transmitting[device_id] = True
            print(f"Dispositivo {device_id} está transmitindo...")
        
        # Simula o tempo de transmissão
        time.sleep(TRANSMISSION_TIME)
        
        # Verifica se houve uma colisão
        with lock:
            if transmitting.count(True) > 1:
                # Colisão detectada
                print(f"Colisão detectada com o dispositivo {device_id}. Tentando novamente...")
                transmitting[device_id] = False
                time.sleep(COLLISION_WAIT_TIME + random.uniform(0, 1))
            else:
                # Transmissão concluída com sucesso
                transmitting[device_id] = False
                print(f"Dispositivo {device_id} terminou a transmissão com sucesso.")

def main():
    # Inicializa os dispositivos
    threads = []
    for device_id in range(NUM_DEVICES):
        t = threading.Thread(target=device_transmission, args=(device_id,))
        threads.append(t)
        t.start()
    
    # Aguarda todos os dispositivos terminarem
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
