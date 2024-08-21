import os
import socket
import struct
import time
import select
import sys

# define o tipo de mensagem ICMP (8 == echo request(ping))
ICMP_ECHO_REQUEST = 8

def checksum(source_string):
    '''
    Calcula o checksum para garantir a integridade dos dados no pacote ICMP.
    Lógica:
        - A função soma os valores de todos os bytes do pacote, inverte os bits do 
        resultado e retorna o checksum
    '''
    sum = 0
    count_to = (len(source_string)//2) * 2
    count = 0

    while count < count_to:
        this_val = source_string[count+1] * 256 + source_string[count]
        sum = sum + this_val
        sum = sum & 0xffffffff
        count = count + 2

    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer   

def create_packet(id):
    '''
    Criação do pacote ICMP
    '''
    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, 0, id, 1)
    data = struct.pack('d', time.time())
    my_checksum = checksum(header + data)

    header = struct.pack('bbHHh', ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), id, 1)
    return header + data

def receive_ping(sock, id, timeout):
    '''
    Espera a resposta do pacote ICMP enviado.
    '''
    time_left = timeout
    while True:
        start_time = time.time()
        ready = select.select([sock], [], [], time_left)
        time_spent = (time.time() - start_time)
        if ready[0] == []:
            return

        time_received = time.time()
        recv_packet, addr = sock.recvfrom(1024)
        icmp_header = recv_packet[20:28]
        type, code, checksum, packet_id, sequence = struct.unpack('bbHHh', icmp_header)

        if packet_id == id:
            bytes_in_double = struct.calcsize('d')
            time_sent = struct.unpack('d', recv_packet[28:28 + bytes_in_double])[0]
            return time_received - time_sent

        time_left = time_left - time_spent
        if time_left <= 0:
            return

def ping(dest_addr, timeout=1):
    '''
    Função principal que realiza o ping.
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.settimeout(timeout)

    packet_id = os.getpid() & 0xFFFF
    packet = create_packet(packet_id)
    sock.sendto(packet, (dest_addr, 1))

    delay = receive_ping(sock, packet_id, timeout)
    sock.close()

    if delay is None:
        print(f"Ping to {dest_addr} timed out.")
    else:
        print(f"Ping to {dest_addr} took {delay * 1000:.2f} ms.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ping.py <ip_address>")
        sys.exit(1)

    dest_addr = sys.argv[1]
    print(f"Pinging {dest_addr}...")
    ping(dest_addr)