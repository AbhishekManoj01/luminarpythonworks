#start with kl



from re import fullmatch
user_input=input("enter registration number")
pattern="(KL|kl)[0-9]{2}[A-Z]{1,2}[0-9]{4}"
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("invalid")
else:
    print("valid")
