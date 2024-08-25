class VLAN:
    def __init__(self, id_vlan):
        self.id_vlan = id_vlan
        self.dispositivos = []

    def add_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def __str__(self):
        return f"VLAN {self.id_vlan}: {[dispositivo.endereco_mac for dispositivo in self.dispositivos]}"


class Dispositivo:
    def __init__(self, endereco_mac, vlan):
        self.endereco_mac = endereco_mac
        self.vlan = vlan
        vlan.add_dispositivo(self)

    def envia_mensagem(self, destinatario_mac, mensagem):
        if self.vlan.pode_comunicar(destinatario_mac):
            print(f"Dispositivo {self.endereco_mac} na VLAN {self.vlan.id_vlan} envia mensagem para {destinatario_mac}: {mensagem}")
        else:
            print(f"Dispositivo {self.endereco_mac} na VLAN {self.vlan.id_vlan} não pode comunicar com {destinatario_mac}")


class Rede:
    def __init__(self):
        self.vlans = {}

    def add_vlan(self, id_vlan):
        if id_vlan not in self.vlans:
            self.vlans[id_vlan] = VLAN(id_vlan)

    def get_vlan(self, id_vlan):
        return self.vlans.get(id_vlan, None)

    def add_dispositivo(self, endereco_mac, id_vlan):
        vlan = self.get_vlan(id_vlan)
        if vlan:
            return Dispositivo(endereco_mac, vlan)
        else:
            print(f"VLAN {id_vlan} not found")
            return None

    def get_dispositivos(self, id_vlan):
        vlan = self.get_vlan(id_vlan)
        if vlan:
            return vlan.dispositivos
        return []

    def pode_comunicar(self, remetente_mac, destinatario_mac):
        vlan_remetente = None
        vlan_destinatario = None
        for vlan in self.vlans.values():
            for dispositivo in vlan.dispositivos:
                if dispositivo.endereco_mac == remetente_mac:
                    vlan_remetente = vlan
                if dispositivo.endereco_mac == destinatario_mac:
                    vlan_destinatario = vlan
        return vlan_remetente == vlan_destinatario


# Cria a rede e adicionar VLANs
Rede = Rede()
Rede.add_vlan(10)
Rede.add_vlan(20)

# Adiciona dispositivos às VLANs
dispositivo1 = Rede.add_dispositivo('00:1A:2B:3C:4D:5E', 10)
dispositivo2 = Rede.add_dispositivo('00:1A:2B:3C:4D:5F', 10)
dispositivo3 = Rede.add_dispositivo('00:1A:2B:3C:4D:60', 20)

# Testa a comunicação
dispositivo1.envia_mensagem('00:1A:2B:3C:4D:5F', "Hello from dispositivo1")  # Deve ser possível
dispositivo1.envia_mensagem('00:1A:2B:3C:4D:60', "Hello from dispositivo1")  # Deve ser impossível
dispositivo3.envia_mensagem('00:1A:2B:3C:4D:5F', "Hello from dispositivo3")  # Deve ser impossível
dispositivo3.envia_mensagem('00:1A:2B:3C:4D:60', "Hello from dispositivo3")  # Deve ser possível
