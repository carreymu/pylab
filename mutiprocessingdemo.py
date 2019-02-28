import multiprocessing as mp
import time

# when you have lots of tasks, use pool
def job(x):
    return x*x

def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(10))
    print(res)

# input core number
def muliticore(coreNum):
    pool = mp.Pool(processes=coreNum)
    res = pool.map(job, range(100))
    print(res)

def mutilicores(coreNum):
    pool = mp.Pool(processes=coreNum)
    res = pool.map(job, range(100))
    print(res)
    res = pool.apply_async(job, (17, ))
    print(res.get())
    res1 = [pool.apply_async(job, (i,)) for i in range(100)]
    print([r.get() for r in res1])

def func(msg):
    print("msg:", msg)
    time.sleep(3)
    print("end:", msg)
    return msg

def multiprocess(coreNum):
    pool = mp.Pool(processes=coreNum)
    res = []
    for i in range(coreNum):
        msg = 'hello %d' % i
        res.append(pool.apply_async(func, (msg, )))
    print('Starting tasks ...')
    pool.close()
    pool.join()
    print([r.get() for r in res])
    print('Sub-processing is done.')


# when you have few tasks, the simple way is using process
def do(n):
    # get processing name
    name = mp.current_process().name
    print(name, 'starting')
    print('worker', n)
    return

def processing_few_tasks(n):
    num_list = []
    for i in range(n):
        p = mp.Process(target=do, args=(i, ))
        num_list.append(p)
        p.start()
        p.join()
        print('Process ended')

if __name__ == '__main__':
    # muticore()
    # muliticore(3)
    # mutilicores(4)
    # multiprocess(4)
    processing_few_tasks(4)