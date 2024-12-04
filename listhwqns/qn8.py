arr1=[10,12,11,14,15,16,9]
arr2=[20,21,10,11,14,9]
arr1.sort()
arr2.sort()
p1=0
p2=0
while((p1<=len(arr1)-1 )and (p2<=len(arr1)-1)):
    if arr1[p1]==arr2[p2]:
        print(arr1[p1])
        p1+=1
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
    elif arr1[p1]>arr2[p2]:
        p2+=1
