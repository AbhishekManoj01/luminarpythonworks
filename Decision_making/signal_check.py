signal=input("Enter the signal :").lower()

if signal=="red":
    print("STOP")
elif signal=="green":
    print("GO..")
elif signal=="yellow":
    print("WAIT..!")
    
else:
    print("Undefined signal")