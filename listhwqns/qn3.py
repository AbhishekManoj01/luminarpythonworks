arr=[6,3,5,8,5,7]
arr.sort()
print("input array: ",arr)
duplicate=arr.copy()
for i in range (0,len(arr)-1):
    j=i+1
    sub=arr[j]-arr[i]
    if sub==0:
        if arr[j] in duplicate:
            ind=duplicate.index(arr[j])
            duplicate.pop(ind)
print(duplicate[len(duplicate)-2])