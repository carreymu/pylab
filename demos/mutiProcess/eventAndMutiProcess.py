import time
import random
from multiprocessing import Process, Queue, Event

class P1(Process):

    def __init__(self, queue, event):
        self.queue = queue
        self.event = event
        super(P1, self).__init__()
    
    # Overwrite method run
    def run(self):
        self.event.wait()
        print('P1 put ...')
        for i in range(5):
            time.sleep(random.randint(1,3))
            self.queue.put(i)
            print('put: P1 -> %s' % i)

class P2(Process):
    def __init__(self, queue, event):
        self.queue = queue
        self.event = event
        super(P2, self).__init__()
    # Overwrite method run
    def run(self):
        # Block, waiting for main process singnal
        self.event.wait()
        print('P2 read ...')
        while 1:
            i = self.queue.get()
            print('get: P2 -> %s' % i)

if __name__ == "__main__":
    queue = Queue()
    event = Event()
    p1 = P1(queue, event)
    p2 = P2(queue, event)
    p1.start()
    p2.start()

    # Main process blocks 3 seconds.
    print('Sleep 3s...')
    time.sleep(3)
    event.set()

    # 
    p1.join()
    p2.terminate()