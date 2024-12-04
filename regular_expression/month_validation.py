from re import fullmatch
pattern="(0)?[1-9]|1[0-2]"
user_input=input("enter the variable name")
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("invaid")
else:
    print("valid")