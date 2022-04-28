from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()
# even though we define run method we call object by start method 
#it is due to predefine start method.
t1.start()
sleep(.02)
t2.start()
#join method helps to join the threads before main threads
t1.join()
t2.join()

print('Bye')