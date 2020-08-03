import multiprocessing
import threading
import time


def count(num):
    time.sleep(1)  ## 模拟IO操作
    print("Process {0} End".format(num))


if __name__ == '__main__':
    start_time = time.time()
    process = list()
    for i in range(5):
        p = multiprocessing.Process(target=count, args=(i,))
        # p = threading.Thread(target=count, args=(i,))
        process.append(p)

    for p in process:
        p.start()

    for p in process:
        p.join()

    end_time = time.time()
    print("Total time:{0}".format(end_time - start_time))