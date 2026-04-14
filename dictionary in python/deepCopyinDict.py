import copy

student = {
    "name":"sita",
    "age": 20,
    "phnum":{
        "mob1": 9999,
        "mob2": 7777
        },
    "addr":{
        "present":"bang",
        "prem": "mysore"
    }
}

s1 = student # shall copy
s2 = copy.deepcopy(student) # deep copy

student["addr"]["prem"] = "Hyd"

print(student["addr"]["prem"]) # Hyd
print(s1["addr"]["prem"]) # Hyd
print(s2["addr"]["prem"]) # mysore