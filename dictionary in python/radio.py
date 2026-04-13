class Radio:
    def turnOn(self,x):
        if (x==1):
            print("Radio is on")
        else:
            print("Radio is off")
class Car:
    def __init__(self,min,max):
        self.cmin=min
        self.cmax=max
        self.r=Radio()
c=Car(60,120)
print(c.cmin)
print(c.cmax)
c.r.turnOn(2)
c.r.turnOn(1)
