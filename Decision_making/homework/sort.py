num1=int(input("Enter the first number  :"))
num2=int(input("Enter the second number :"))
num3=int(input("Enter the third number  :"))
# total=num1+num2+num3

# if num1>num2 and num1>num3:
#     large=num1
# elif num2>num3:
#     large=num2
# else:
#     large=num3

# if num1<num2 and num1<num3:
#     small=num1
# elif num2<num3:
#     small=num2
# else:
#     small=num3
    
# sec_large=total-(large+small)

# print(f"Sorting order {small},{sec_large},{large}")

if num1>num2 and num1>num3:
    if num2>num3:
      print(f"Sorting order {num1},{num2},{num3}")
    else:
      print(f"Sorting order {num1},{num3},{num2}")
elif num2>num1 and num2>num3:
    if num1>num3:
      print(f"Sorting order {num2},{num1},{num3}")
    else:
      print(f"Sorting order {num2},{num3},{num1}")
elif num3>num1 and num3>num2:
    if num1>num2:
      print(f"Sorting order {num3},{num1},{num2}")
    else:
      print(f"Sorting order {num3},{num2},{num1}")