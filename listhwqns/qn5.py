arr=[1,1,2,2,3,4]
temp=[]
for i in range(len(arr)-1,-1,-1):
    temp.append(arr[i])
print(temp)