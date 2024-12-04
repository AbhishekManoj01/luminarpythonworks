arr=[4,6,3,2,5]
print("Method 1")
print(max(arr))
print(min(arr))

print("Method 2")
small=arr[0]
big=arr[0]
for i in range(len(arr)):
    if arr[i]<small:
        small=arr[i]
    if arr[i]>big:
        big=arr[i]
print(small)
print(big)

print("Method 3")
arr.sort()
print(arr[0])
print(arr[len(arr)-1])