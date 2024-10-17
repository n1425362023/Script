import asyncio


async def request(url):
    print(url + "请求成功")


def fun_callback(task):
    print(task.result())


c = request("https://www.baidu.com")
new_loop = asyncio.new_event_loop()
asyncio.set_event_loop(new_loop)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
print(task)
task.add_done_callback(fun_callback)
loop.run_until_complete(task)
print(task)
