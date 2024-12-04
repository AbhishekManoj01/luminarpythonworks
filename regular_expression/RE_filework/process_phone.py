from re import fullmatch
f=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\regular_expression\\RE_filework\\phone_no.txt")
for line in f:
    phone=line.strip("\n")
    pattern="(91)?[0-9]{10}"
    matcher=fullmatch(pattern,phone)
    if matcher!=None:
        print(phone)
