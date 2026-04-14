import pickle
class Student:
    def __init__(self,name,age,height,addr):
        self.name=name
        self.age=age
        self.height=height
        self.addr=addr
    def display(self):
        print(self.name)
        print(self.age)
        print(self.height)
        print(self.addr)
f=open("names.txt","rb")
s=pickle.load(f)
s.display()
print("Object is retrievd")
f.close()