arr=[1,2,2,2,1,4,4,5]
arr.sort()
duplicate_elements=[]
for i in range(0,len(arr)-1):
    j=i+1
    result=arr[j]-arr[i]
    if result==0:
        if arr[i] not in duplicate_elements:
            duplicate_elements.append(arr[i])
           
print(duplicate_elements)