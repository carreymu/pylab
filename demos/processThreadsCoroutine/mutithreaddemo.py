import multiprocessing
import threading
import time

n = 0


def count(num):
    global n
    for i in range(100000):
        n += i
    print("Process {0}:n={1},id(n)={2}".format(num, n, id(n)))


if __name__ == '__main__':
    start_time = time.time()

    process = list()
    for i in range(5):
        # p = multiprocessing.Process(target=count, args=(i,))  # 测试多进程使用
        p = threading.Thread(target=count, args=(i,))  # 测试多线程使用
        process.append(p)

    for p in process:
        p.start()

    for p in process:
        p.join()

    # 变量n在进程p{0,1,2,3,4}和主进程（main）中均拥有唯一的地址空间
    print("Main:n={0},id(n)={1}".format(n, id(n)))
    end_time = time.time()
    print("Total time:{0}".format(end_time - start_time))