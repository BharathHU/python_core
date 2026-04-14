import copy
a=[10,20,30,40,[50]]
print(a)
a1=a #shallow copy
b1=copy.deepcopy(a)#deep copy
print(a1)
print(b1)
a[4][0]=100
print(a)
print(a1)
print(b1)