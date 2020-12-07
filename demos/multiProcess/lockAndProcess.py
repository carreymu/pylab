from multiprocessing import Process, Lock

class P1(Process):
    def __init__(self, lock, fp):
        self.lock = lock
        self.fp = fp
        super(P1, self).__init__()
    def run(self):
        # Only one proess does their job
        with self.lock:
            # print('~~P1 is coming~~')
            for i in range(5):
                f = open(self.fp, 'a+')
                f.write('p1 - %s\n' % i)
                f.close()

class P2(Process):
    def __init__(self, lock, fp):
        self.lock = lock
        self.fp = fp
        super(P2, self).__init__()

    def run(self):
        with self.lock:
            # print('~~P2 is coming~~')
            for i in range(5):
                f = open(self.fp, 'a+')
                f.write('p2 - %s\n' % i)
                f.close()
if __name__ == "__main__":
    # lock
    lock = Lock()
    fp = 'lock.txt'
    p1 = P1(lock, fp)
    p2 = P2(lock, fp)

    p1.start()
    p2.start()

    p1.join()
    p2.join()