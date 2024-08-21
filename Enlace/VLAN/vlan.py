class VLAN:
    def __init__(self, vlan_id):
        self.vlan_id = vlan_id
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def __str__(self):
        return f"VLAN {self.vlan_id}: {[device.mac_address for device in self.devices]}"


class Device:
    def __init__(self, mac_address, vlan):
        self.mac_address = mac_address
        self.vlan = vlan
        vlan.add_device(self)

    def send_message(self, recipient_mac, message):
        if self.vlan.can_communicate(recipient_mac):
            print(f"Device {self.mac_address} in VLAN {self.vlan.vlan_id} sends message to {recipient_mac}: {message}")
        else:
            print(f"Device {self.mac_address} in VLAN {self.vlan.vlan_id} cannot communicate with {recipient_mac}")


class Network:
    def __init__(self):
        self.vlans = {}

    def add_vlan(self, vlan_id):
        if vlan_id not in self.vlans:
            self.vlans[vlan_id] = VLAN(vlan_id)

    def get_vlan(self, vlan_id):
        return self.vlans.get(vlan_id, None)

    def add_device(self, mac_address, vlan_id):
        vlan = self.get_vlan(vlan_id)
        if vlan:
            return Device(mac_address, vlan)
        else:
            print(f"VLAN {vlan_id} not found")
            return None

    def get_devices(self, vlan_id):
        vlan = self.get_vlan(vlan_id)
        if vlan:
            return vlan.devices
        return []

    def can_communicate(self, sender_mac, recipient_mac):
        sender_vlan = None
        recipient_vlan = None
        for vlan in self.vlans.values():
            for device in vlan.devices:
                if device.mac_address == sender_mac:
                    sender_vlan = vlan
                if device.mac_address == recipient_mac:
                    recipient_vlan = vlan
        return sender_vlan == recipient_vlan


# Criar a rede e adicionar VLANs
network = Network()
network.add_vlan(10)
network.add_vlan(20)

# Adicionar dispositivos às VLANs
device1 = network.add_device('00:1A:2B:3C:4D:5E', 10)
device2 = network.add_device('00:1A:2B:3C:4D:5F', 10)
device3 = network.add_device('00:1A:2B:3C:4D:60', 20)

# Testar a comunicação
device1.send_message('00:1A:2B:3C:4D:5F', "Hello from device1")  # Deve ser possível
device1.send_message('00:1A:2B:3C:4D:60', "Hello from device1")  # Deve ser impossível
device3.send_message('00:1A:2B:3C:4D:5F', "Hello from device3")  # Deve ser impossível
device3.send_message('00:1A:2B:3C:4D:60', "Hello from device3")  # Deve ser possível
