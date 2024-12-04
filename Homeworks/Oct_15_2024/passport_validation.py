from re import fullmatch
pattern=r"[A-Z]{1}[1-9]{1}[0-9]{1}\s?[0-9]{4}[1-9]{1}"
user_input=input("Enter passport number:")
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("Invalid")
else:
    print("valid")