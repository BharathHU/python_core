try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
    print(c)
except ValueError as e:
    print("It is value Error")
except ZeroDicisionError as e:
    print("It is ZeroDivisionError")
except Exception as e:
    print("It is a Error")
print("Program Ended")