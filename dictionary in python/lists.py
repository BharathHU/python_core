a=[]
i=0
while True:
    n=int(input("Enter a n:"))
    a.insert(i,n)
    i+=1
    print("Do you wish to Countinue")
    print("press 1: Yes")
    print("press 2: No")
    choice=int(input("Enter your choice:"))
    if choice==1:
        continue
    else:
        break
print(f"enterd elements in list are: {a} ")