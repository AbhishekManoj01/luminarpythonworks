arr=[2,3,8,9,4,5]
searched_ele=int(input("enter the value to be searched"))

arr.sort()
lower=0
upper=len(arr)-1
is_present=False

while(lower<=upper):
    mid=(lower+upper)//2

    if searched_ele==arr[mid]:
        is_present=True
        break

    elif searched_ele < arr[mid]:
        upper=mid-1

    elif searched_ele > arr[mid]:
        low=mid+1
        
print(is_present)
