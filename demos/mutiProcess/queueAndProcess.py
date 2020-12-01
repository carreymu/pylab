import time
import random
from multiprocessing import Process, Queue

class P1(Process):
    def __init__(self, queue, group=None):
        self.queue = queue
        super(P1, self).__init__(group=None,)
    def run(self):
        # Input data
        print('~~P1 put ~~')
        for i in range(5):
            time.sleep(random.randint(1, 3))
            self.queue.put(i)
            print('put: P1 -> %s' %i )

class P2(Process):
    def __init__(self, queue, group=None):
        self.queue = queue
        super(P2, self).__init__(group=None,)

    def run(self):
        # Read data
        print('~~P2 read~~')
        while 1:
            i = self.queue.get()
            print('get: P2 -> %s' % i)

if __name__ == "__main__":
    # create queue for process P1 and P2
    queue = Queue()

    # create process
    p1 = P1(queue)
    p2 = P2(queue)

    # start process
    p1.start()
    p2.start()

    # Main process waits for process P1
    p1.join()

    # Kill P2, it's an endless loop
    p2.terminate()



