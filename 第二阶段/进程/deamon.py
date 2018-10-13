# p.daemon 默认值为False,表示主进程运行结束后不会影响子进程的
# 运行，知道子进程运行完，进程才结束。
# 如果设置为Ture,则主进程运行完成，子进程一起退出。
# 该属性不是把进程设置为linux/unix中的守护进程


import multiprocessing as mp
import time

def fun():
    print("start")
    time.sleep(4)
    print("end")


p = mp.Process(target = fun)
p.deamon = True
p.start()
# p.join()

print("****main process over****")
