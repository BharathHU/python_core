a=int(input("Enter a:"))
b=int(input("Enter b:"))
try:
    c=a/b
    print(c)
except Exception as e:
    print("Error in program")
    print(e)
print("Program is Ended")