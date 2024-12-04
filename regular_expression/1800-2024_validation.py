from re import fullmatch
pattern="((18|19[0-9]{2}|200[0-9]|201[0-9]|202[0-4]))"
user_input=input("enter the year")
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("invaid")
else:
    print("valid")