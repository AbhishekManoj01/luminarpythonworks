#10 digit
from re import fullmatch
user_input=input("enter the number")
pattern="(91)?[0-9]{10}"                          #  ? optional 91 veram/verathirikam
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("invalid")
else:
    print("valid")