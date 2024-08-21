import random

def fragmentar_pacote(pacote, mtu):
    """Fragmenta um pacote de dados em fragmentos menores.
    
    Args:
        pacote (bytes): O pacote de dados a ser fragmentado.
        mtu (int): O tamanho máximo de cada fragmento.
        
    Returns:
        list: Lista de fragmentos do pacote.
    """
    fragmentos = [pacote[i:i + mtu] for i in range(0, len(pacote), mtu)]
    return fragmentos

def transmitir_fragmentos(fragmentos, taxa_perda):
    """Simula a transmissão de fragmentos com possíveis perdas.
    
    Args:
        fragmentos (list): Lista de fragmentos a serem transmitidos.
        taxa_perda (float): Probabilidade de perda de um fragmento (0.0 a 1.0).
        
    Returns:
        list: Lista de fragmentos recebidos.
    """
    fragmentos_recebidos = []
    for fragmento in fragmentos:
        if random.random() > taxa_perda:  # Verifica se o fragmento não é perdido
            fragmentos_recebidos.append(fragmento)
    return fragmentos_recebidos


def reagrupar_fragmentos(fragmentos, total_pacote):
    """Reagrupa fragmentos no destino, tentando reconstruir o pacote original.
    
    Args:
        fragmentos (list): Lista de fragmentos recebidos.
        total_pacote (int): Tamanho total do pacote original.
        
    Returns:
        bytes: Pacote reconstruído ou None se a reconstrução falhar.
    """
    if not fragmentos:
        return None

    # Ordena os fragmentos (assume que são ordenados, pode-se incluir um identificador)
    fragmentos.sort()
    pacote_reconstruido = ''.join(fragmentos)

    # Verifica se o pacote reconstruído é do tamanho esperado
    if len(pacote_reconstruido) == total_pacote:
        return pacote_reconstruido
    else:
        return None


# Dados de entrada
pacote_original = 'Este eh um pacote de dados muito grande que precisa ser fragmentado e reagrupado.'
mtu = 20  # Tamanho máximo de cada fragmento
taxa_perda = 0.05  # 20% de chance de perda de um fragmento

# Fragmentação
fragmentos = fragmentar_pacote(pacote_original, mtu)
print(f'Fragmentos: {fragmentos}')

# Transmissão
fragmentos_recebidos = transmitir_fragmentos(fragmentos, taxa_perda)
print(f'Fragmentos recebidos: {fragmentos_recebidos}')

# Reagrupamento
pacote_reconstruido = reagrupar_fragmentos(fragmentos_recebidos, len(pacote_original))
if pacote_reconstruido:
    print(f'Pacote reconstruído: {pacote_reconstruido}')
else:
    print('Falha na reconstrução do pacote.')