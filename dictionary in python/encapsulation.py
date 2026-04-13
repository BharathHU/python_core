#ENCAPSULATION
class Book:
    def __init__(self,value):
        self.__pages=value
    def setter(self,value):
        if (value>=1):
            self.__pages=value
    def getter(self):
        return self.__pages
d1=Book(100)
d1.setter(114)
res=d1.getter()
print(res)
d1.setter(-99)
res1=d1.getter()
print(res1)