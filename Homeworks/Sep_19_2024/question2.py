arr=[1,2,1,1,2,3,4,5,1]
arr.sort()
print(arr)
duplicate=arr.copy()
for i in range(0,len(arr)-1):
    j=i+1
    sub=arr[j]-arr[i]
    if sub==0:
        if arr[j] in duplicate:
            ind=duplicate.index(arr[j])
            duplicate.pop(ind)
print(duplicate)