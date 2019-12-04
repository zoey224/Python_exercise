import time
import threading

def hello(name, t):
    """线程函数"""

    for i in range(10):
        print("hello, i am %s" %name)
        time.sleep(t)

def demo():
    A = threading.Thread(target=hello, args=('A', 1), name='A')
    B = threading.Thread(target=hello, args=('B', 2), name='B')
    C = threading.Thread(target=hello, args=('C', 3), name='C')

    #C.setDaemon(True)  # 设置子线程在主线程结束时是否无条件跟随主线程一起退出

    A.start()
    A.join(5)
    B.start()
    C.start()

    time.sleep(20)

    print('进程A%s' % ('还在工作中' if A.isAlive() else '已经结束',))
    print('进程B%s' % ('还在工作中' if B.isAlive() else '已经结束',))
    print('进程C%s' % ('还在工作中' if C.isAlive() else '已经结束',))

    print('下班了')

if __name__ =='__main__':
    demo()