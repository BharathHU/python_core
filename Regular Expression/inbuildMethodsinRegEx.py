# match():
# method checks for a match only at the beginning of the string, 
import re
text="Python is super easy"
regEx=r"Python"
result=re.match(regEx,text)
print(result)


# search():
# while search() method checks for a match anywhere in the string but it consider 1st occuring substring. 
import re
text="Python is super easy"
regEx=r"easy"
result=re.search(regEx,text)
print(result)

#findall(:
# findall() method finds all the matches of the pattern in the string and returns them as a list.
import re
text="If you still want to keep brute force (for learning), you can break early when product becomes zero. " \
"This is because if any of the numbers is zero, the product will be zero regardless of the other numbers."
regEx=r"a"
result=re.findall(regEx,text,re.IGNORECASE)
print(result)
#re.IGNORECASE
#used to ignore case sensitivity. It will match the pattern regardless of whether it is in uppercase or lowercase.