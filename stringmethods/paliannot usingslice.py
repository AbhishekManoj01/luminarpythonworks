text=input('enter the text')
rev_string=""
length=len(text)-1
for i in range(length,-1,-1):
    rev_string=rev_string + text[i]
print(rev_string)