arr=[100,200,300,400,500,600,700,800,900]
# odd_pos=[arr[i] for i in range(len(arr)) if i%2!=0]
# odd_pos=[number for index,number in enumerate(arr) if index%2!=0]
# odd_pos.reverse()
# print(odd_pos)
l=1
r=len(arr)-1
if r%2==0:
    r=r-1
while(l<=r):
    arr[l],arr[r]=arr[r],arr[l]
    l=l+2
    r=r-2
print(arr)
    
# for index,num in enumerate(odd_pos):
#     arr[index+1]=num
# print(arr)


# j=0
# for i in range(len(arr)):
#     if i%2!=0:
#         arr[i]=odd_pos[j]
#         j+=1
# print(arr)

# for i in range(1,len(arr),2):
#     arr[i]=odd_pos.pop()
# print(arr)