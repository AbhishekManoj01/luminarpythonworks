n=input("enter the string to be checked")
def is_paliandrome(n):
    n1=n
    rev=0
    i=0
    temp=True
    while(i<=n):
        rem=n%10
        rev=rev*10+rem
        n=n/10
    if n1==rev:
        print("true")
    else:
        print("false")
