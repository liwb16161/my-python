#!/usr/local/bin/python3

import multiprocessing as mp
import time



def th1():
    time.sleep(1)
    print("1111111")


def th2():
    time.sleep(2)
    print("2222222")

def th3():
    time.sleep(60)
    print("3333333")

things = [th1,th2,th3]
Process = []

for th in things:
    p = mp.Process(target = th)
    Process.append(p)

for p in Process:
    p.start()
    print(p.name,p.pid)


# 内核会帮助应用层子进程的状态
for i in Process:
    i.join(timeout = 1)
