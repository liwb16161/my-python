#!/usr/local/bin/python3

import socket
import sys


HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

#创建
sockfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定
sockfd.bind(ADDR)

while True:
    data,addr = sockfd.recvfrom(1024)
    print("receive from %s:%s"%\
        (addr,data.decode()))
    sockfd.sendto("收到消息".encode(),addr)

sockfd.close()
