arr=[2,3,4,5]
sum=7
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)): 
     s= arr[i]+arr[j]
     if sum==s:
            print(arr[i],arr[j])
    break