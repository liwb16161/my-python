import multiprocessing as mp
import time
def fn(n):
    time.sleep(1)
    print(n*n)


test = [1,2,3,4,5,6]
pool = mp.Pool(processes = 4)

pool.map(fn,test)
