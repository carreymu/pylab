import os
import time
import random
from multiprocessing import Queue
from threading import Thread, Condition

def producer(queue, condition):
    for i in range(5):
        # Get lock
        if condition.acquire():
            if not queue.empty():
                condition.wait()
            i = random.randint(1, 5)
            queue.put(i)
            print(f'thread:{os.getpid()},producer -> {i}')
            # Waking other threads
            condition.notify()
            # Release lock
            condition.release()
            time.sleep(1)

def consumer(queue, condition):
    for i in range(5):
        # Get lock
        if condition.acquire():
            if queue.empty():
                condition.wait()
            i = queue.get()
            print(f'thread:{os.getpid()},consumer ->{i}')
            condition.notify()
            condition.release()
            time.sleep(1)

if __name__ == "__main__":
    queue = Queue()
    condition = Condition()
    t1 = Thread(target=producer, args=(queue, condition))
    t2 = Thread(target=consumer, args=(queue, condition))
    t1.start()
    t2.start()
    t1.join()
    t2.join()