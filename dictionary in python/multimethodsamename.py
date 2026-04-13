#declare multiple methods by using same name by using properties functions.
class Person:
    def __init__(self):
        self.__name=" "
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
    getset=property(getter,setter)
p=Person()
p.getset="rama"
res=p.getset
print(res,end=" ")
p.getset="seeta"
res=p.getset
print(res)
p.getset="Bharath weds Pinki"
res=p.getset
print(res)