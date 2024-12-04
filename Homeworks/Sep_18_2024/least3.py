arr=[1,2,3,4,5]
l=arr[0]
for i in range(0,(len(arr))+1):
    if l not in arr:
        print(l)
        break
    l+=1