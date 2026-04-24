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
