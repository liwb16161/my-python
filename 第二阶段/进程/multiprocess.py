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
    time.sleep(3)
    print("3333333")

p1 = mp.Process(target = th1)
p2 = mp.Process(target = th2)
p3 = mp.Process(target = th3)


p1.start()
p2.start()
p3.start()


p1.join()
p2.join()
p3.join()
