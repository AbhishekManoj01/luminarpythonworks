number=int(input("enter number "))
is_prime=True
for i in range(2,number):
    if number%i==0:
        is_prime=False
        break
    
if is_prime==False:
    print("not a prime number")
else:
    print("prime number")

