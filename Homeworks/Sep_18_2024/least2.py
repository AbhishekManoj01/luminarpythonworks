arr=[1,2,3,5]
l=arr[0]
for i in range(len(arr)):
    if l!=arr[i]:
        print(l)
        break
    l+=1