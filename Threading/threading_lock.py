import time
import threading

lock = threading.Lock()
counter = 0

def hello():
    """线程函数"""

    global counter

    if lock.acquire(): # 请求互斥锁，如果被占用，则阻塞，直至获取到锁
        time.sleep(0.2) # 假装思考
        counter += 1
        print("我是第%d个"%counter)

    lock.release() # 释放互斥锁，否则后果很严重，在本例中不释放就卡在 我是第1个

def demo():
    threads = list()
    for i in range(30):
        threads.append(threading.Thread(target=hello))
        threads[-1].start()

    for t in threads:
        t.join()
        # 主线程处理完其他的事务后，需要用到子线程的处理结果，
        # 也就是主线程需要等待子线程执行完成之后再结束，这个时候就要用到join()方法

    print('统计完毕，共有%d人'%counter)

if __name__=='__main__':
    demo()