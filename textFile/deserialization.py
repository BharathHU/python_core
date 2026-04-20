#deserialization is the process of recreating the object from the saved file is called de-serialization or unplicking.
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
e=pickle.load(f)
e.display()
f.close()
print("Object is saved into text file")
