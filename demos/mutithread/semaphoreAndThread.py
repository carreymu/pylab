import os
import time
from threading import Thread, Semaphore

semaphore = Semaphore(4)

def task(name):
    if semaphore.acquire():
        print(f'thread:{os.getpid()}, name:{name}, sleep 1...')
        time.sleep(1)
        semaphore.release()

if __name__ == "__main__":
    ts = []
    for i in range(10):
        t = Thread(target=task, args=(f't {i}', ))
        ts.append(t)
        t.start()
    for t in ts:
        t.join()