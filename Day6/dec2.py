def decoratorFunc (welcome):
    def a():
        print("Start")
        welcome()
        print("End")
    return a

def subFunc():
    print("Sub fn")

subFunc = decoratorFunc(subFunc)

subFunc()

'''--------------------------------'''

import time
import math

def calculate_time(func):

    def inner(*args, **kwargs):

        begin = time.time()

        func(*args, **kwargs)

        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(10)
