arr=[1,2,2,2,1,3,4,5]
arr.sort()
print("with duplicates: ", arr)
duplicate=arr.copy()
for i in range (0,len(arr)-1):
    j=i+1
    sub=arr[j]-arr[i]
    if sub==0:
        if arr[j] in duplicate:
            ind=duplicate.index(arr[j])
            duplicate.pop(ind)
print("without duplicates:",duplicate)