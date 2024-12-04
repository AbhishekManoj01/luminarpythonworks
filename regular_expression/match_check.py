#starting with an alphabet fron p-t
# in second place must be a numbear that is \ by 3
#followed by anynumber alphabets,number,@
from re import fullmatch
pattern="[p-tP-T][369][a-zA-Z0-9@]"
user_input=input("enter the variable name")
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("invaid")
else:
    print("valid")