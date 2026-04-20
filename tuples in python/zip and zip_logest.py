from itertools import zip_longest
names=["dhoni","kohli","klr","hp"]
jnum=[7,18,1,33]
runs=[5000,8500,3000,6000]
team=["csk","rcb"]
# print(names[0],jnum[0],runs[0],team[0])
# print(names[1],jnum[1],runs[1],team[1])
# print(names[2],jnum[2],runs[2],team[2])
# print(names[3],jnum[3],runs[3],team[3])
res=list(zip_longest(names,jnum,runs,team,fillvalue="*"))
for i in res:
    print(i)