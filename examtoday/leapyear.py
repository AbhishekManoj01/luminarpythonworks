yr=int(input("enter the year "))
if (yr % 100 != 0 and yr % 4 == 0) or( yr % 100 == 0 and yr % 400 == 0) :
    print(f"{yr} is a leap year")
else:
    print(f"{yr} is not a leap year")