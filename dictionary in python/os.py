class Os:
    def __init__(self):
        self.status=True
        print("OS is installing")
    def getOs(self):
        print("OS is still installing")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=Os()
        print("Mobile is created")
        print("With OS installed")
m=Mobile("iphone")
print(m.mname)
print(m.o.status)
# temp=m
del m
print("After delete")
print(m.mname)
print(m.o.status)