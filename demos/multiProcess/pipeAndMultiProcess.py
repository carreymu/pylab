import time
import random
from multiprocessing import Process, Pipe

class P1(Process):
    def __init__(self, pipe):
        self.pipe = pipe
        super(P1, self).__init__()

    # Overwrite method run
    def run(self):
        # P1 sends message
        print('P1 sends...')
        for i in range(3):
            time.sleep(random.randint(1,2))
            self.pipe.send(i)
            print('send: P1 -> %s' % i)

class P2(Process):
    def __init__(self, pipe):
        self.pipe = pipe
        super(P2, self).__init__()

    # Overwrite method run
    def run(self):
        # P2 receives
        print('P2 receives')
        for i in range(3):
            i = self.pipe.recv()
            print('recv: P2 -> %s' % i)
    
        # P2 sends...
        print('P2 sends...')
        for i in range(3):
            time.sleep(random.randint(1,2))
            self.pipe.send(i)
            print('Send: P2 -> %s' % i)

if __name__ == "__main__":
    pp1, pp2 = Pipe()
    p1, p2 = P1(pp1), P2(pp2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
