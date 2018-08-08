from multiprocessing import  Process
import time
import os

class MyProcess(Process):
    def __init__(self,value):
        Process.__init__(self)
        self.value = value

    def run(self):
        n = 5
        for i in range(n):
            print("now time is {},{},mypid is {}".format(i,time.ctime(),os.getpid()))
            time.sleep(3)


p = MyProcess(3)
p.start()
p.join()
