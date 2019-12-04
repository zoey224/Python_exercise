import time
import threading
import random


cond =threading.Condition() # 创建条件对象
draw_Seeker = False
draw_Hider = False

def seeker():

    global draw_Seeker, draw_Hider

    time.sleep(1)
    cond.acquire()
    time.sleep(random.random())
    print("Seeker:我已经蒙上眼了")
    cond.notify()
    cond.wait()

    print("Seeker:来找你了")
    cond.notify()
    cond.release()
    time.sleep(random.randint(3,10))

    if draw_Hider:
        print("Seeker:抓到你啦")
    else:
        draw_Seeker=True
        print("Seeker:找不到你我认输了")

def hider():
    global draw_Seeker, draw_Hider

    cond.acquire()
    cond.wait()
    time.sleep(random.random())
    print("Hider:我藏好了")
    cond.notify()
    cond.wait()


    cond.release()
    time.sleep(random.randint(3, 10))

    if draw_Seeker:
        print("Hider:哈哈，没找到，我赢啦")
    else:
        draw_Hider = True
        print("Hider:我认输,自己出来")

def demo():
    th_seeker = threading.Thread(target=seeker)
    th_hider = threading.Thread(target=hider)
    th_seeker.start()
    th_hider.start()

    th_seeker.join()
    th_hider.join()

if __name__=='__main__':
    demo()


