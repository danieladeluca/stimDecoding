import socket
import time
import threading


#  TPC/IP Communication
TCP_ip = '192.168.1.2'      # IP address of the recording machine
TCP_port = 40000            # 
TCP_buffSize = 4096


tcpObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpObj.connect((TCP_ip, TCP_port))

while 1:
    time.sleep(3)
    tcpObj.send(b"123123\n")

# while 1:
    # msg = tcpObj.recv(TCP_buffSize)
    # print(msg.decode('utf8'))
    