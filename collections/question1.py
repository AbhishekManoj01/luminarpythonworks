arr=[1,3,4,5]
n=arr[0]
for i in range((len(arr))+1):
    if n not in arr:
        print(n)
        break
    
    n+=1
    