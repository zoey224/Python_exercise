import time
import threading

S=threading.Semaphore(5)

def use_resources(d):
    S.acquire()
    time.sleep(1)
    print('%d号用完释放资源'%d)
    S.release()

def demo():
    threads = list()
    for i in range(30):
        threads.append(threading.Thread(target=use_resources,args=(i,)))
        threads[-1].start()


    for t in threads:
        t.join()

    print("Done")

if __name__=='__main__':
    demo()