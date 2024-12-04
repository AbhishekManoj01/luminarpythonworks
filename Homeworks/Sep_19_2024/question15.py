print("Method 1")
arr=[1,2,4,5,7,6,9,2]
border=len(arr)//2
lst1=[]
lst2=[]
for i in range(len(arr)):
    if i<border:
        lst1.append(arr[i])
    elif i>=border:
        lst2.append(arr[i])
print(arr)
print(lst1)
print(lst2)

print("Method 2")
arr=[1,2,4,5,7,6,9,2]
border=len(arr)//2
lst1=arr[:border]
lst2=arr[border:]
print(arr)
print(lst1)
print(lst2)