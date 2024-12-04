print("Method 1")
arr=[1,6,3,7]
temp=[]
for i in range(len(arr)):
    val=arr.pop()
    temp.append(val)
print(temp)

print("Method 2")
arr=[1,6,3,7]
temp=[]
for i in range(len(arr)-1,-1,-1):
    temp.append(arr[i])
print(temp)
