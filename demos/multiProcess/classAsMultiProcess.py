import os
import random
import time
from multiprocessing import Process

# Class P inherits Process
class P(Process):

    #Overrides the Run method
    def run(self):
        s = random.randint(1, 10)
        print('pid: %s, name: %s, sleep %s...' % (os.getpid(), self.name, s))
        time.sleep(s)

if __name__ == '__main__':
    # create 5 process and execute them
    ps = []
    for i in range(5):
        p = P()
        ps.append(p)
        p.start()
    
    # main process execution after end of subprocess
    for p in ps:
        print('main pid: %s' % os.getpid() )
        p.join()