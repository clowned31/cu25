import socket
import random

UDP_IP_ADDRESS = "85.100.192.158"
UDP_PORT_NO = 5005

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Gonderilecek toplam veri boyutu
TOTAL_DATA_SIZE = 83886080  # 80 MB

# Gonderilecek paket boyutu
PACKET_SIZE = 83886080  # 1500 byte, tipik Ethernet MTU boyutu




while True:
    
    data = bytes([random.randint(0, 255) for _ in range(PACKET_SIZE)])
    
    # Veriyi gonderin
    clientSock.sendto(data, (UDP_IP_ADDRESS, UDP_PORT_NO))
    
    
    
    
    print("Toplam {} byte ({:.2f} MB) veri gonderildi.".format(TOTAL_DATA_SIZE, TOTAL_DATA_SIZE / (1024 * 1024)))