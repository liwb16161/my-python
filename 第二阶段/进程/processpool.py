import multiprocessing as mp
import time
import os

result = []
def worker(msg):
    time.sleep(2)
    print(msg)
    return ("0000","success")

pool = mp.Pool(processes = 4)


for i in range(10):
    msg = "hello %d"%(i)
    # 向进程池加入要执行的事件,不按顺序
    # apply_async(func,args=(1,),kvargs={})
    r = pool.apply_async(worker,(msg,))
    result.append(r)
    # 按顺序
    # pool.apply(worker,(msg,))
for res in result:
    print(res.get())

# 关闭进程池事件加入通道
# 即不能再向进程池中加入事件
pool.close()
# 阻塞等待进程池处理事件结束后回收进程池
pool.join()
