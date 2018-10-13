#!/usr/local/bin/python3

import socket


#创建流式套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',8888))

#设置监听
sockfd.listen(5)

#等待连接
while  True:
    connfd,addr = sockfd.accept()
    print("Connect from",addr)
    print("peername",connfd.getpeername())

    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("Receive:",data.decode())

        n = connfd.send(b'receive your message')
        print("发送了%d字节"%n)
    connfd.close()

sockfd.close()
