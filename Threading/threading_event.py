import time
import threading


E = threading.Event()

def work(id):

    print('<%d号员工>上班打卡'%id)
    if E.is_set():
        print('<%d号员工>迟到'%id)
    else:
        print('<%d号员工>等待上班划水中。。' % id)
        E.wait()

    print('<%d号员工>开始工作'%id)
    time.sleep(10)
    print('<%d号员工>下班了' % id)

def demo():
    E.clear()
    threads = list()

    for i in range(3):
        threads.append(threading.Thread(target=work, args=(i,)))
        threads[-1].start()

    time.sleep(5)
    E.set()

    time.sleep(5)
    threads.append(threading.Thread(target=work, args=(9,)))
    threads[-1].start()

    for t in threads:
        t.join()

    print('都下班了')

if __name__ == '__main__':
    demo()

