class Animal:
    def eat(self):
        print("Animal is Eating")
    def breath(self):
        print("Animal is Breating")
    def sleep(self):
        print("Animal is sleeping")
class Tiger(Animal):
    def eat(self):
       print("Tiger Hunt and Eat")
class Monkey(Animal):
    def eat(self):
       print("Monkey will steel and Eat")
class Deer(Animal):
    def eat(self):
       print("Deer will graze and Eat")
t=Tiger()
m=Monkey()
d=Deer()
t.eat()
t.breath()
t.sleep()
m.eat()
m.breath()
m.sleep()
d.eat()
d.breath()
d.sleep()