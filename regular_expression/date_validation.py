from re import fullmatch
date="[1-9]|0[1-9]|1[0-9]|2[0-9]|3[01]"#"(0?[1-9]|[12][0-9]|3[01])"
user_input=input("enter the date")
matcher=fullmatch(date,user_input)
if matcher==None:
    print("invaid")
else:
    print("valid")