import asyncio
import random

async def task_coroutine(pid):
    await asyncio.sleep(random.randint(0,2))
    print("Task %s done" % pid)
async def concurrently():
    tasks = [task_coroutine(i) for i in range(1, 10)]
    await asyncio.gather(*tasks)
asyncio.run(concurrently())