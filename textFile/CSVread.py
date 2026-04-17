import csv
fname=input("Enter file name:")
fptr=open(fname,"r")
data1=csv.reader(fptr)
for i in data1:
    print(i)