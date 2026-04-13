class Heart:
    def __init__(self,name):
        self.hname=str
        print("Heart is alive")
    def getHeart(self):
        print("Get Heart")
class Person:
    def __init__(self,name):
        self.pname=name
        self.h=Heart("xyz")
        self.c1=" "
        print("Person is ready")
        print("With Heart connected")
    def hasPerson(self,c):
        self.c1=c
        print("Person and heart is connected")
class Car:
    def __init__(self,name):
        self.cname=name
        print("Car is ready")
    def getCar(self):
        print("car is ready to drive")
p=Person("abc")
cf=Car("Benzz")
p.hasPerson(cf)
p.c1.getCar()
print(p.pname)
print(p.h.hname)
print(p.c1.cname)
print(p.h.hname)
del p
print(cf.cname)
cf.getCar()