import random
import socket
from socket import *
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('192.168.216.128', 12000))
while True:
    rand = random.randint(0, 10)
    message, address = s.recvfrom(1024)
    message = message.upper()
    if rand < 4:
        continue
    s.sendto(message, address)

