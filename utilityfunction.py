weight_in_kg=int(input("68enter the weight in kg"))
height_in_cm=int(input("enter the height in cm"))
height_in_mtr=height_in_cm/100
bmi=round(weight_in_kg/height_in_mtr**2,2)
print(bmi)
