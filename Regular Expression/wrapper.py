def fun2():
    n=1
    while (n<=10):
        sqr=n*n
        yield sqr
        n=n+1
res=fun2()
print(res.__next__)
print(res. __next__())
print(res. __next__())
print(res. __next__())
print(res. __next__())
