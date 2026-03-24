#线程，进程
#进程是资源单位，每一个进程至少要有一个线程
#线程是执行单位，线程是进程的子单位，线程是进程的资源单位

# 启动每一个程序默认都会有一个主线程

#多线程
from threading import Thread

# def func():
#     for i in range(1000):
#         print('线程1:', i)

# if __name__ == '__main__':
#     t = Thread(target=func)#创建线程并给线程安排任务
#     t.start() #多线程状态为可以开始工作状态，具体的执行时间由CPU决定
#     for i in range(1000):
#         print('主线程:', i)

# class MyThread(Thread):
#     def run(self): #重写run方法  固定的  ->  当线程被执行的时候，被执行的就是run()
#         for i in range(1000):
#             print('线程1:', i)

# if __name__ == '__main__':
#     t = MyThread()#创建线程并给线程安排任务
#     # t.run() # 方法的调用 . ->单线程 .start() ->多线程
#     t.start() #多线程状态为可以开始工作状态，具体的执行时间由CPU决定
#     for i in range(1000):
#         print('主线程:', i)

def func(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    t1 = Thread(target=func, args=('陈粒',))#创建线程并给线程安排任务 
    #这传递的参数是元组  如果只有一个参数  逗号不能省略
    t1.start() #多线程状态为可以开始工作状态，具体的执行时间由CPU决定
 
    t2 = Thread(target=func, args=('陈奕迅',))
    t2.start()