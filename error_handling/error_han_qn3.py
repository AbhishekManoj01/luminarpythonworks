num1=int(input("enter the first numbers"))
num2=int(input("enter the second numbers"))
try:
    result=num1/num2
    print(result)
except:
    num2=int(input("enter the num2 value"))
    result=num1/num2
    print(result)
finally:
    print("file write")
    print("database commit")