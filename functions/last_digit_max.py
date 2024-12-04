def last_digit_max(num1,num2):
    last_num1=num1%10
    last_num2=num2%10
    if last_num1>last_num2:
        return num1
    else:
        return num2

number1=int(input("Enter the first number :"))
number2=int(input("Enter the second number :"))
l_max=last_digit_max(number1,number2)
print(l_max)


#is_prime
#factorial
