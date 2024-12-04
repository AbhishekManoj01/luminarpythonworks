a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>b and a>c and b>c:
    print(f"{b } is second largest")
elif a>b and a>c and c>b:
    print(f"{c} is second largest")
elif b>a and b>c and a>c:
    print(f"{a} is second largest")
elif b>a and b>c and c>a:
    print(f"{c} is second largest")
elif c>a and c>b and a>b:
    print(f"{a } is second largest")
elif c>a and c>b and b>a:
    print(f"{b} is second largest")

