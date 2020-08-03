import time
import asyncio


async def coroutine():
    await asyncio.sleep(1) ## 模拟IO操作


if __name__ == "__main__":
    start_time = time.time()

    loop = asyncio.get_event_loop()
    tasks = []
    for i in range(5):
        task = loop.create_task(coroutine())
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    end_time = time.time()
    print("total time:", end_time - start_time)