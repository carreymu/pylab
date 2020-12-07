import threading

def run(name):
    for i in range(3):
        print('%s --> %s' %(name, i))

if __name__ == "__main__":
    # Create 2 threads
    t1 = threading.Thread(target=run, args=('t1', ))
    t2 = threading.Thread(target=run, args=('t2', ))

    # Start
    t1.start()
    t2.start()

    # Main thread is waiting for other threads
    t1.join()
    t2.join()