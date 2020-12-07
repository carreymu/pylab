from concurrent.futures import ProcessPoolExecutor

def task_batch(total):
    # CPU monster
    num = 0
    for i in range(total):
        num += i
    return num

def task_single(total):
    num = 0
    for i in range(total):
        num += i
    return num

if __name__ == "__main__":
    # Processpool
    pool = ProcessPoolExecutor(max_workers=5)
    # Put tasks into pool
    result_batch = pool.map(task_batch, [100, 1000, 10000, 100000])
    # Output result
    for item in result_batch:
        print(f'item: {item}')
    
    print('=======submit task one by one======')
    results = []
    results.append(pool.submit(task_single, 100))
    results.append(pool.submit(task_single, 1200))
    results.append(pool.submit(task_single, 300))
    results.append(pool.submit(task_single, 400))

    for item in results:
        print(f'item: {item.result()}')
    