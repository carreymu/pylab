import threading

class A(threading.Thread):

    # Overwrite methrd run
    def run(self):
        for i in range(5):
            print('name:%s, %s' %(self.name, i))

if __name__ == "__main__":
    a1 = A()
    a2 = A()
    # Start
    a1.start()
    a2.start()

    a1.join()
    a2.join()