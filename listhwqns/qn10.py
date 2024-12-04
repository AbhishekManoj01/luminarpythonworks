arr=[1,4,5,6,7,8]
num=int(input("enter the number to be removed"))
ind=arr.index(num)
arr.pop(ind)
print(arr)