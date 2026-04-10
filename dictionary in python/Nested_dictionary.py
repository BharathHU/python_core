student={'Name':'sita',
         'age':22,
         'ph_num':{'mobile1':99999999,
                  'mobile2':98765432},
         'Add':{'present':'Bengluru',
                'parm':'Hallera mane'} }
print(student)
print(student['age'])
print(student['ph_num']['mobile1'])
print(student['ph_num']['mobile2'])
print(student['Add']['parm'])

student['Marks']={1:20,2:30,3:40,4:50}
print(student)