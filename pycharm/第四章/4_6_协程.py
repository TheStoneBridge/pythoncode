# # import time

# # def func():
# #     print("1")
# #     time.sleep(3) # 让当前的线程处于阻塞状态，CPU是不为我工作的
# #     print("2")

# # if __name__ == '__main__':
# #     func()

# # input() 程序 也是处于阻塞状态
# # request.get()  在网络请求返回数据之前，程序处于阻塞状态
# # 一般情况下，当程序处于IO操作的时候，程序处于阻塞状态

# #协程: 当程序遇见IO操作的时候，可以选择性的让出CPU的执行权，等IO操作完成之后，再继续执行程序
# # 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# #在宏观上，我们能看到的其实是多个任务在同时进行
# #多任务异步操作

# #上方所讲的一切，都是单线程环境下的协程






# # python编写 协程的程序
# # import asyncio

# # async def func():
# #     print("你好，坤宝")

# # if __name__ == '__main__':
# #     g = func() # 此时的函数时异步协程函数，此时函数执行得到的是一个协程对象
# #     # print(g)
# #     asyncio.run(g)  #协程程序运行需要asyncio模块的支持

# import time
# import asyncio
# async def func1():
#     print("你好，坤宝")
#     # time.sleep(3) # 当程序出现了同步操作的时候，异步就中断了
#     await asyncio.sleep(3)  #异步操作的代码 挂起 3秒钟
#     print("你好，坤宝")

# async def func2():
#     print("你好，冲宝")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("你好，冲宝")

# async def func3():
#     print("你好，金宝")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("你好，金宝")        
    
# async def main():
#     tasks = [
#         asyncio.create_task(func1()),  # 将协程对象封装为任务对象
#         asyncio.create_task(func2()),
#         asyncio.create_task(func3())
#     ]
#     await asyncio.wait(tasks)    
    #  也可以替代为await asyncio.gather(func1(),func2(),func3())
    #asyncio.gather()更简洁   asyncio.wait()（灵活性更高）
    
    
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2-t1)
#     #在 Python 3.11+ 版本中，asyncio.wait() 不再支持直接传入协程对象（coroutine），必须显式封装为任务对象（Task）
#     # ，否则会触发 TypeError: Passing coroutines is forbidden, use tasks explicitly. 错误。



#在爬虫领域的应用

import asyncio

async def  download(url):
    print(f'开始下载')
    await asyncio.sleep(3)
    print(f'下载完成')

async def main():
    urls = ['http://www.baidu.com', 'http://www.sina.com', 'http://www.163.com']
    tasks = [asyncio.create_task(download(url)) for url in urls]
    await asyncio.wait(tasks)
    
if __name__ == '__main__':
    asyncio.run(main())