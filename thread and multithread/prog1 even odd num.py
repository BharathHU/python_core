#Write a multi Threading program to print all the even and odd number within the given range continously.
from threading import Thread
import time
class Even(Thread):
    def run(self):
        print("Even numbers are:")
        for i in range(1,100):
            if i%2==0:
                print(i,"is even")
                time.sleep(0.2)
class Odd(Thread):
    def run(self):
        print("Odd numbers are:")
        for i in range(1,100):
            if i%2!=0:
                print(i,"is odd")
                time.sleep(0.2)
e=Even()
o=Odd()
e.start(),o.start()
e.join(),o.join()
print("Executed Successfully")
