import time
class Demo:
    def print_names(self):
        names=["Rama","Krishna","Arjuna"]
        for i in names:
            print(i)
        time.sleep(2)
    def print_nums(self):
        for i in range(10):
            print(i)
            time.sleep(0.6)
    def print_sum(self):
        a=100
        b=200
        c=a+b
        print(c)
        time.sleep(0.8)
d=Demo()
d.print_names()
d.print_nums()
d.print_sum()

    