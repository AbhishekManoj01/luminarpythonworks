#3 alphabets
#4th place alphabet [P/C/A/F/H/T]
# 1 alphabet
#4digit
#1alphabet
from re import fullmatch
pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"
user_input=input("Enter pan number:")
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("Invalid")
else:
    print("valid")