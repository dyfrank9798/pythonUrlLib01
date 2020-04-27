#异步爬虫
import requests
import time
import aiohttp
import asyncio
URL= 'https://morvanzhou.github.io/'

# def normal():
#     for i in range(2):
#         r = requests.get(URL)
#         url = r.url
#         print(url)
#
# t1 = time.time()
# normal()
# print("Normal total time:"+ time.time()-t1)



async def job(session):
    response = await session.get(URL)
    # print (response.url)
    return str(response.url)


async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks =[loop.create_task(job(session)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]
        print(all_results)

t1 = time.time()
loop = asyncio.get_event_loop()#获取loop
loop.run_until_complete(main(loop))#loop去执行main
print("Async total time:", time.time() - t1)

# loop = asyncio.get_event_loop()
# task = loop.create_task(fun())
# loop.run_until_complete(task)