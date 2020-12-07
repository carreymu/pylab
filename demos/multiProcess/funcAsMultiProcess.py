import os
import time
import random 
from multiprocessing import Process

# Using Process(target=func, args=(arg1, arg2...)) to create a process
# Using function as process
def task(name):
    s = random.randint(1, 10)
    print('pid: %s name: %s, sleep: %s ..' % (os.getpid(), name, s))
    time.sleep(s)

if __name__ == '__main__':
    # create 5 subprocess and execute them
    ps = []
    for i in range(5):
        p = Process(target=task, args=('p%s' % i,))
        ps.append(p)
        p.start()
    
    # main process execution after end of subprocess
    for p in ps:
        print('main pid: %s' % os.getpid() )
        p.join()