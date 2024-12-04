weight=int(input("Enter the weight in kg:"))
height=int(input("Enter the height in cm:"))
age=int(input("Enter the age :"))
gender=int(input("Enter 1 for male \nEnter 2 for female\nEnter your choice:"))

if gender==1:
    bmr=(10*weight)+6.25*height-5*age+5
elif gender==2:
    bmr=(10*weight)+6.25*height-5*age-161
else:
    print("error")
print(bmr)
print("1 .sedentary (little or no exercise)\n2 .lightly active (light exercise/sports 1-3 days/week)\n3 .moderately active (moderate exercise/sports 3-5 days/week)\n4 .very active (hard exercise/sports 6-7 days a week) \n5 .extra active (very hard exercise/sports & physical job or 2x training)")
activity=int(input("Enter your choice :"))

if activity==1:
    calorie=bmr*1.2
elif activity==2:
    calorie=bmr*1.375
elif activity==3:
    calorie=bmr*1.55
elif activity==4:
    calorie=bmr*1.725
elif activity==5:
    calorie=bmr*1.9
else:
    print("Wrong selection")

print(f"The number of calories need to maintain weight {calorie}")

print("For weight gain press 1 \nFor weight loss press 2")
choice=int(input("Enter your choice :"))   
target_weight=int(input("Enter the target weight :"))
duration=int(input("Enter the number of weeks :"))
calorie_change=target_weight*7700
days=duration*7
daily_calorie_change=calorie_change/days
if choice==1:
    print(f"daily calorie increase :{daily_calorie_change}")
elif choice==2:
    print(f"daily calorie decrease :{daily_calorie_change}")
else:
    print("Error")
