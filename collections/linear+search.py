arr=[2,4,5,6,3,8,9]
search_element=int(input("enter number to be searched"))
is_present=False
for i in range(0,len(arr)):
    if arr[i]==search_element:
        is_present=True
        break
if is_present==True:
    print(search_element,"is found")
else:
 print("not found")
