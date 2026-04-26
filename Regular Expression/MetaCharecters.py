# 1.( . )Dot metacharecter
# 2. \ Escape metacharecter
# 3. | pipe metacharecter
# 4. * Star metacharecter
# 5. + Plus metacharecter
# 6. ? Question mark metacharecter
# 7. ^ Hat metacharecter
# 8. $ Dollar metacharecter
# 9. [] Square brackets metacharecter
# 10. () Parenthesis metacharecter
# 11. {} Curly brackets metacharecter

# ( . )Dot metacharecter:
# it will search for all the charecter in the string and the values are return with in the list.
print("( . )Dot metacharecter:")
import re 
text="Python is a language."
regEx=r"."
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#================================================================================
# (\) Escape metacharecter:
# it is used to search meta charecters. it treats meta charecters as actual symbols not as special commands.
print("(\) Escape metacharecter:")
import re 
text="Python is a language."
regEx=r"\."
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#==================================================================================
#(|) pipe metacharecter:
# basically it works like or either it will match left side substring or it will match right side substring.
print(" | pipe matacharecter:")
import re 
text="a Python is a ython pppython"
regEx=r"is|super"
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#==================================================================================
import re 
text="Python is a language"
regEx=r"is| "
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#===================================================================================
import re 
text="Python is a super"
regEx=r"is|"
result=re.findall(regEx,text,re.IGNORECASE)
print(result)

#====================================================================================
# * metacharecter:
# it is will check the occurence of charecter for 0 or more time (0 - ∞).
print("* metacharecter:")
import re 
text="Python is a language pppython not ython and pppppppython"
regEx=r"p*ython"
result=re.findall(regEx,text,re.IGNORECASE)
print(result)

#======================================================================================
# + metacharecter:
# It will check the occurence of the charecter for one or more time (1 - ∞).
print("+ metacharecter:")
import re 
text="Python is a language pppython not ython and pppppppython"
regEx=r"p+ython"
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#======================================================================================
#  ? metacharecter:
# It will check the occurence of the cherecter for 0 or 1 time(0 - 1).
print("? metacharecter:")
import re 
text="Python is pppython not ython and pppppppython"
regEx=r"p?ython"
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#======================================================================================
#  ^ metacharecter:
# It is used to search the pattern at the beginning of the string.
print("^ metacharecter:")
import re 
text="a Python is pppython not ython and pppppppython"
regEx=r"^a"
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#========================================================================================
# $ metacharecter:
# It is used to search the pattern at the end of the string.
print("$ metacharacter:")
import re 
text="a Python is pppython not ython and pppppppython"
regEx=r"pppppppython$"
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#=========================================================================================
# [] Square brackets metacharecter:
# any charecter declare inside square bress it will search for the particular charcter in the string.
print("[] square bracket metacharecter:")
import re 
text="a Python is pppython not ython and pppppppython"
regEx=r"[aeiou]"
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#=========================================================================================
#{} curly brackets metacharecter:
# It is used to specify the number of occurence of the charecter. by using {},or
# we can declare the occurence of the charecter min and max time.
print("{} square bracket metacharecter:")
import re 
text="a Python is pppython not ython and pppppppython"
regEx=r"p{2,3}ython" # limite only applicable for p
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#===========================================================================================
import re 
text="a Python is pppython not ython and pppppppython"
regEx=r"p{,2}ython" # limite only applicable for p
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#===========================================================================================
import re 
text="a Python is pppython not ython and pppppppython"
regEx=r"p{2}ython" # limite only applicable for p
result=re.findall(regEx,text,re.IGNORECASE)
print(result)