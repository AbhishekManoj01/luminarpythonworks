num1=int(input("enter number1 "))
num2=int(input("enter number 2 "))
max_num=max(num1,num2)
for i in range (max_num,(num1*num2)+1,max_num):
    if i%num1==0 and i%num2==0:
        print(i)
        break