# fptr=open("car.jpg","rb")
# data=fptr.read()
# print(data)
# for byte in data:
#     print(format(byte,"08b"),end="")

fptr=open("car.jpg","rb")
data=fptr.read()
fptr1=open("car.jpg","wb")
fptr1.write(data)
fptr.close()
fptr1.close()
print("Reference of the image has created!")