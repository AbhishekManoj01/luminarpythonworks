def multiplication_table(number,n=10):
    for i in range(1,n+1):
        print(f"{i} X {number} = {i*number}")
num=int(input("Enter the number :"))
#limit=int(input("Enter the limit :"))
multiplication_table(num)