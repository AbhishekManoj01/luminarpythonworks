arr=[2,3,4,5]
sum=7
left=0
right=len(arr)-1
while(left<right):
    curr_sum=arr[left]+arr[right]
    if curr_sum==sum:
        print(arr[left],arr[right])
        break
    elif curr_sum>sum:
        right=right-1
    elif curr_sum<sum:
        left=left+1

