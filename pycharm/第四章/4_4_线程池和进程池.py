# 线程池:  一次性开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度由线程池完成
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def fn(name):
    for i in range(1000):
        print(name, i)

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as pool:
        for i in range(10): 
            pool.submit(fn, name=f"线程{i}")
    #  等待线程池中的任务全部执行完毕，才继续执行下面的代码（守护线程）
    print("主线程结束")