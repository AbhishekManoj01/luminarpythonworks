print("Method 1")
arr=[1,2,4,5,7,6]
#to replace 4 with 9
ind=arr.index(4)
arr[ind]=9
print(arr)

print("Method 2(user input)")
arr=[1,2,4,5,7,6]
ind=int(input("Enter the index:"))
if ind>=0 or ind<len(arr):
    val=int(input("Enter the user input :"))
    arr[ind]=val
    print(arr)
else:
    print("Index does not exist")