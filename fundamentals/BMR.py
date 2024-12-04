height=int(input("enter the height in cm "))
weight=int(input("enter the weight in kg "))
age=int(input("enter the age "))
gender=input("enter gender ").lower()
print(f"{height},{weight},{age},{gender}")
if gender =="male":
     BMR=10 * weight + 6.25 * height - 5 * age + 5
elif gender=="female":

     BMR=10 * weight + 6.25 * height - 5 * age - 161
else:
    print("enter a valid gender")

print(BMR)
activitylevel=int(input(""" 
             select acvtivity level
            press 1 for sedentary
            press 2 for lightely active
            press 3 for moderatively active 
            press 4 for very active 
            press 5 for extra active
                        """       ))
if activitylevel==1:
 calories=BMR*1.2
elif activitylevel==2:
 calories=BMR*1.375
elif activitylevel==3:
 calories=BMR*1.55
elif activitylevel==4:
 calories=BMR*1.75
elif activitylevel==5:
 calories=BMR*1.9
else:
   print("select a valid choice for activity level")
print(f"total number of caolories you need in order to maintain yuor current weight={calories} ")
print("""select
      enter 1 for weight gain
      enter 2 for weight loss
      """)


target_weight=int(input("enter weight to reduce in kg "))
duration=int(input("enter duration in weeks "))
calory_deficit=target_weight*7700
days=duration*7
daily_calories=calory_deficit/days
print(f"daily calory deficit={daily_calories}")