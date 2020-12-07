import time
import random
import os
from multiprocessing import Process, Queue, Condition

# todo: blocked

def producer(queue, condition):
    while 1:
        if condition.acquire():
            if not queue.empty():
                # Waiting for another process
                condition.wait()
            i = random.randint(1, 5)
            queue.put(i)
            print('pid:%s, producer -> %s' % (os.getpid(), i))
            # Waking other process
            condition.notify()
            # Release lock
            condition.release()
            time.sleep(1)

def consumer(queue, condition):
    while 1:
        # Get lock
        if condition.acquire():
            if queue.empty():
                # Waiting for another process
                condition.wait()
            i = queue.get()
            print('pid:%s, consumer -> %s' % (os.getpid(), i))
            # Waking other process
            condition.notify()
            # Release lock
            condition.release()
            time.sleep(1)

if __name__ == "__main__":
    queue = Queue()
    condition = Condition()
    p1 = Process(target=producer, args=(queue, condition))
    p2 = Process(target=consumer, args=(queue, condition))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    