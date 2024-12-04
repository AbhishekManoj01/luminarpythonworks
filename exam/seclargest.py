a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>b and a>c :
    if b>c:
        print(f"{b} is second largest")
    else:
        print(f"{c} is second largest")
elif b>a and b>c:      
    if a>c:
        print(f"{a} is second largest")
    else:
       print(f"{c} is second largest")
elif  c>a and c>b:
    if a>b:
        print(f"{a} is second largest")
    else:
        print(f"{b} is second largest")