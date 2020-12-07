import os
import random
import time
from multiprocessing import Pool

# Create a pool with 5 processes and execute program.
# It's efficient when cpu core number equals process number.
def task(name):
    s = random.randint(1, 10)
    print('pid: %s, name:%s, sleep:%s ...' % (os.getpid(), name, s))
    time.sleep(s)

if __name__ == "__main__":
    # Create a process pool with 5 processes
    pool = Pool(5)

    # Run 10 tasks
    for i in range(10):
        pool.apply_async(task, ('p-%s' % i, ))
    
    # Closing pool first
    pool.close()
    pool.join()
