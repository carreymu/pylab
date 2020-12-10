from concurrent.futures import ProcessPoolExecutor

def task(total):
    # Simulate CPU intensive operations
    num = 0
    for i in range(total):
        num += i
    return num

if __name__ == "__main__":
    # Process pool
    pool = ProcessPoolExecutor(max_workers=5)
    # Batch tasks for the pool
    result = pool.map(task, [100, 1000, 10000, 100000])
    # Output
    for item in result:
        print(item)
    print("*" * 30)

    results = []
    results.append(pool.submit(task, 100))
    results.append(pool.submit(task, 10000))
    results.append(pool.submit(task, 100000))
    results.append(pool.submit(task, 1000000))
    for future in results:
        print(future.result())