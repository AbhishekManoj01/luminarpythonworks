num=int(input("Enter the number:"))

# if (num%3==0) and (num%5==0) and (num%15==0):
#     print("fizzbuzz")
# elif num%3==0:
#     print("fizz")
# elif num%5==0:
#     print("buzz")
# else:
#     print("invalid")

if num%15==0:
    print("fizzbuzz")
elif num%5==0:
    print("buzz")
elif num%3==0:
    print("fizz")
else:
    print("invalid")