import os
import time
import random
from multiprocessing import Queue
from threading import Thread

class T1(Thread):
    def __init__(self, queue):
        self.queue = queue
        super(T1, self).__init__()
    
    def run(self):
        print('T1 put...')
        for i in range(5):
            time.sleep(random.randint(1, 2))
            self.queue.put(i)
            print(f'thread: {os.getpid()}, put:T1 -> {i}')
    

class T2(Thread):
    def __init__(self, queue):
        self.queue = queue
        super(T2, self).__init__()
    
    def run(self):
        print('T2 read...')
        while self.is_alive():
            i = self.queue.get()
            print(f'thread: {os.getpid()}, get:T2 -> {i}')
    def terminate(self):
        self.__is_running = False

if __name__ == "__main__":
    # Create queue
    queue = Queue()

    # Create threads
    t1 = T1(queue)
    t2 = T2(queue)

    # start
    t1.start()
    t2.start()

    # Stoping T2 after 5 seconds
    time.sleep(5)
    t2.terminate()

    t1.join()
    t2.join()