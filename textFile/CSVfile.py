import csv
fname=input("Enter file name: ")
fptr=open(fname,"w")
w=csv.writer(fptr)
w.writerow(["Eid","Ename","Edes","Esal","Eaddr"])
for i in range(3):
    eid=input("Enter EID: ")
    ename=input("Enter Ename: ")
    edes=input("Enter Edes: ")
    esal=input("Enter Esal: ")
    eaddr=input("Enter Eaddr: ")
    w.writerow([eid,ename,edes,esal,eaddr])
fptr.close()
print("5 Employee Details are stored in csv file")