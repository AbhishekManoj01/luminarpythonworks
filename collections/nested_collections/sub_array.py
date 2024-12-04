arr=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
]
list_objects=[]
# for ls in lst:
#     if type(ls)==int:
#         print(ls)
#     else:
#         for i in ls:
#           lst1.append(i)  
# print(lst1)

# for ls in lst:
#     if(isinstance(ls,list)==True):
#         list_objects.append(ls)
# print(list_objects)
list_objects=[ls for ls in arr if isinstance(ls,list) ]

# Method 1 for finding max length item
# max_list=max(list_objects,key=lambda ls:len(ls))
# method 2 for finding max length item
max_list=max(list_objects,key=len)
print(max_list)
