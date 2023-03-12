import time
from functools import lru_cache

@lru_cache(maxsize=3) #no. of callbacks
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n
#Practice
@lru_cache(maxsize=2)
def another_work(n):
    input("enter any key")
    return n

if __name__ == '__main__':
    print("now running some work")
    # some_work(3)
    # print("done")
    # some_work(4)
    # input("enter your name")
    # some_work(3)
    # print("running again")
    # print("this is third time")
    # some_work(5)
    # print("This is fourth time")
    another_work(3)
    another_work(4)
