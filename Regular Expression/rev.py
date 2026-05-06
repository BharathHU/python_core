#1.
def revStr(str):
    rev = ""
    for ch in str:
        rev = ch + rev
    return rev
s = input("Enter a string: ")
res= revStr(s)
print("Reversed String is:",res)

#2.
def revSentence(sentence):
    words = []
    word = ""
    for ch in sentence:
        if ch != " ":
            word += ch
        else:
            words += [word]
            word = ""
    words += [word]
    rev_sen = ""
    for i in range(len(words) - 1, -1, -1):
        rev_sen += words[i]
        if i != 0:
            rev_sen += " "
    return rev_sen
sentence = input("Enter a sentence: ")
result = revSentence(sentence)
print(result)
#3.
def remove_dup(s):
    res = ""
    for ch in s:
        if ch not in res:
            res += ch       
    return res
s = input("Enter a string: ")
print(remove_dup(s))



