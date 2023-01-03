import asyncio

async def fibo(value):
    if value < 0:
        raise "Negative Number"
    a, b = 0, 1
    for i in range(2, value+1):
        a, b = b, a+b
    
    return b

async def runner(values: list[int]):
    requests = [asyncio.create_task(fibo(number)) for number in values]
    done, pending = await asyncio.wait(requests)
    
    results = [res.result() for res in done]
    print('Total Results: {}'.format(len(results)))
    print('Pending Results: {}'.format(len(pending)))
    print(sorted(results))
    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(runner([1, 10, 2, 3, 4, 15, 6]))
    loop.close()