#Serialization the process of 
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
s=Student("Rama",22,5.5,"Bengaluru")
s=Student("Radha",22,5.8,"Mysuru")
f=open("names.txt","w")
pickle.dump(s,f)
print("Object is saved into text file")
f.close()