#validate gmail_id
#lowercase
#start with an alphabet
#numbers optioonal
#@gmail.com
#before @64 characters

from re import fullmatch
pattern="[a-z]+[a-z0-9]{5,9}@gmail.com"
user_input=input("enter the mail id")
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("invaid")
else:
    print("valid")