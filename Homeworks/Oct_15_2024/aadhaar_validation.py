from re import fullmatch
pattern="[2-9]{1}[0-9]{3}\\s[0-9]{4}\\s[0-9]{4}"
user_input=input("Enter aadhaar number :")
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("Invalid")
else:
    print("valid")