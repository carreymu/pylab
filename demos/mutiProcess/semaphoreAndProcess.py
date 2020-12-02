import time
import os
from multiprocessing import Process, Semaphore

# Create 10 processes, only 4 of them do something.

# Maxmum 4 processes for semaphore
semaphore = Semaphore(4)

def task(name):
    if semaphore.acquire():
        print('pid:%s, name:%s, sleep:1 ..' % (os.getpid(), name))
        time.sleep(1)
        semaphore.release()

if __name__ == "__main__":
    ps = []
    for i in range(10):
        p = Process(target=task, args=('p %s' % i, ))
        ps.append(p)
        p.start()
    for p in ps:
        p.join()
    