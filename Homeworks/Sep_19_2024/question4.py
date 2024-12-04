# arr=[1,2,1,1,2,3,4,5,4]
# arr.sort()
# print(arr)
# for i in range(len(arr)-1):
#     if(arr[i]!=arr[i+1]):
#         c=0
#         for num in arr:
#             if arr[i]==num:
#                 c+=1
#         print(f"{arr[i]}={c}")
print("Method 1")
def occ_count(lst,x):
    count=0
    for ele in lst:
        if(ele==x):
            count+=1
    return count
arr=[1,2,1,1,2,3,4,5,4]
arr.sort()
dup=[]
print(arr)
for ele in arr:
    if ele not in dup:
        dup.append(ele)
        c=occ_count(arr,ele)
        print(ele,c)

print("Method 2")
arr=[1,2,1,1,2,3,4,5,4]
dup=[]
for ele in arr:
    if ele not in dup:
        print(ele,arr.count(ele))
        dup.append(ele)