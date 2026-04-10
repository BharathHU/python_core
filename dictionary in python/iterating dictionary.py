student={"Name":"Bharath","Age":22,"Add":"Bengaluru","height":"176cm"}
print(student)
print(len(student))
print(student["Age"])
for i in student:
    print(i)
for i in student.keys():
    print(i)
for i in student:
    print(student[i])
for i in student.values():
    print(i)
for i in student:
    print(i," ",student[i])
for i,j in student.items():
    print(i," ",j)