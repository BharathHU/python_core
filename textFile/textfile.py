print("Enter the Filename:")
fname=input()
fptr=open(fname,"w")
for i in range(5):
    print("Enter the name:")
    data=input()
    fptr.write(data+"\n")
fptr.close()
print("5 names one written to text file")



print("Enter the Filename:")
fname=input()
fptr=open(fname,"a")
for i in range(5):
    eid=input("Enter the eid:")
    enames=input("Enter the enames:")
    edes=input("Enter the edes:")
    esal=input("Enter the esal:")
    eaddrs=input("Enter the eaddrs:")
    fptr.write(eid+"\t"+enames+"\t"+edes+"\t"+esal+"\t"+eaddrs)
    fptr.close()
    print("5 employee details are started in text file")