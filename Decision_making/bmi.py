weight_in_kg=int(input("Enter the weight in kg :"))
height_in_cm=int(input("Enter the height in cm :"))
height_in_metre=height_in_cm/100
bmi=weight_in_kg/height_in_metre**2
bmi=round(bmi)
print(bmi)

if bmi<19:
    print("under weight")
elif bmi>=19 and bmi<25: #bmi<25
    print("normal weight")
elif bmi>=25 and bmi<30: #bmi<30
    print("over weight")
elif bmi>=30:
    print("obese")
else:
    print("invalid")