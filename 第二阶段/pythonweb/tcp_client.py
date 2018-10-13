#!/usr/local/bin/python3

from  socket import *


#创建和服务端相同的套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#发起连接 服务端地址
sockfd.connect(('127.0.0.1',8888))

while True:
    data = input("Msg>>")

    if not data:
        break

    sockfd.send(data.encode())

    data = sockfd.recv(1024)
    print(data.decode())

sockfd.close()
