import os
import time
import random
from multiprocessing import Queue
from threading import Thread, Event

class T(Thread):
    def __init__(self, queue, event):
        self.queue = queue
        self.event = event
        super(T, self).__init__()

class T1(T):
    # def __init__(self, queue, event):
    #     self.queue = queue
    #     self.event = event
    #     super(T1, self).__init__()
    
    def run(self):
        # Blocked , waiting for main thread
        self.event.wait()
        print('T1 put...')
        for i in range(5):
            # time.sleep(random.randint(1, 3))
            self.queue.put(i)
            print(f'Thread: {os.getpid()}, put T1 -> {i}')
class T2(T):
    def run(self):
        # Blocked, waiting for main thread
        print('T2 read ...')
        while self.is_alive:
            i = self.queue.get()
            print(f'Thread: {os.getpid()}, get T2 -> {i}')

    def terminate(self):
        self.__is_running = False

if __name__ == "__main__":
    queue = Queue()
    event = Event()

    t1 = T1(queue, event)
    t2 = T2(queue, event)

    t1.start()
    t2.start()

    # Main thread sleeps 2 seconds
    print('main thread ...')
    time.sleep(1)
    event.set()

    time.sleep(5)
    t2.terminate()

    t1.join()
    t2.join()
