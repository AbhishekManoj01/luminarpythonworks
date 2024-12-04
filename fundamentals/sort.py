a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>b and a>c:
    if b>c:
        print(f"{a},{b},{c}")
    else:
        print(f"{a}{c}{b}")
elif b>a and b>c:      
    if a>c:
        print(f"{b}{a}{c}")
    else:
        print(f"{b}{c}{a}")
elif  c>a and c>b:
    if a>b:
        print(f"{c}{a}{b}")
    else:
        print(f"{c}{b}{a}")