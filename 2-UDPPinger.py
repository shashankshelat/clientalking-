import socket 
from socket import AF_INET, SOCK_DGRAM
import time
ip = '192.168.216.128'
c = socket.socket(AF_INET,SOCK_DGRAM) 
c.settimeout(2) 
count = 1
while count<=10:
    m = 'pinging..' 
    start=time.time() 
    c.sendto(m,(ip, 12000))
    try:
        message, address = c.recvfrom(80)
        elapsed = (time.time()-start) 
        print count
        print m
        print 'RTT calculated is:' + str(elapsed) + " seconds"
    except socket.timeout: # i have taken 2 seconds
        print count
        print 'Request timed out'
    count+=1 
    if count > 10: 
        c.close()
        
