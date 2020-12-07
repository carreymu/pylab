import os
import random
import time
from multiprocessing.pool import ThreadPool

def task(name):
    s = random.randint(1, 10)
    print(f'thread: {os.getpid()}, name:{name}, sleep: {s}')
    time.sleep(s)

if __name__ == "__main__":
    # Create pool with 4 threads
    pool = ThreadPool(4)
    
    # Run 10 tasks
    for i in range(10):
        pool.apply_async(task, (f't-{i}',))
    
    # Close and join
    pool.close()
    pool.join()
