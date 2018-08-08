from multiprocessing import Process
import time

def worker(sec,msg):
    for i in range(3):
        time.sleep(sec)
        print("the worker is ming ")
        print(msg)


p = Process(name = 'worker' ,\
        target = worker,args = (2,), \
        kwargs = {"msg":"my name is bigman"})



p.start()

print("进程名称",p.name)
print("进程pid",p.pid)
print("进程状态",p.is_alive())


p.join()
