import requests
from concurrent.futures import ThreadPoolExecutor

def task(url):
    # Simulate CPU intensive operations
    return requests.get(url).status_code

if __name__ == "__main__":
    # ThreadPool
    pool = ThreadPoolExecutor(max_workers=5)
    # Batch tasks
    urls = ['http://www.baidu.com','http://www.163.com']
    result = pool.map(task, urls)
    # Output
    for item in result:
        print(item)
    print('*'* 30)

    results =[]
    results.append(pool.submit(task, 'http://mail.163.com'))
    results.append(pool.submit(task, 'http://finance.163.com'))
    for future in results:
        print(future.result())