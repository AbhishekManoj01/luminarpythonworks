arr=[100,800,300,600,500,400,700,200]
left=1
right=len(arr)-1
if right%2==0:
    right-=1
while(left<right):
    arr[left],arr[right]=arr[right],arr[left]
    left=left+2
    right=right-2
print(arr)