num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number :"))

if num1==num2==num3:
    print("Numbers are equal")
elif num1>num2 and num1>num3:
    print(f"{num1} is largest")
elif num2>num3:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")
    
# num1>num2 and num1>num3 then num1
# num2>num1 and num2>num3 then num2
# num3>num1 and num3>num2 then num3
# num1==num2==num3 then all are equal