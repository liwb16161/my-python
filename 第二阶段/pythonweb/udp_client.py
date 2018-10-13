#!/usr/local/bin/python3

import socket
import sys


HOST = sys.argv[1]
PORT= int(sys.argv[2])

#服务端ip ,port
ADDR = (HOST,PORT)

#创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(sockfd.fileno())
print(sockfd.family)
print(sockfd.type)
print(sockfd.getsockname())
#收发消息
while True:
    data = input("请输入要发送的消息：")
    sockfd.sendto(data.encode(),ADDR)
    data,addr = sockfd.recvfrom(1024)
    print("从服务端接收：",data.decode())

sockfd.close()
