from re import fullmatch
# pattern=r"([A-Z]{2}-?[0-9]{2}[0-9]{4}[0-9]{7})|([A-Z]{2}[0-9]{2}\s?[0-9]{4}[0-9]{7})"
# pattern="(KL)-([0-7][0-9]|8[0-6])-[0-9]{4}-[0-9]{7}"
user_input=input("Enter license number:")
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("Invalid")
else:
    print("valid")