fptr=open("car.jpg","rb")
data=fptr.read()
print(data)
for byte in data:
    print(byte)