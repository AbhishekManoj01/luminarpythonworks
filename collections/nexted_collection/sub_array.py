# max no of elements in a sub array
lst=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
]
# list_object=[]
# for item in lst:
#     if isinstance(item,list):
#         list_object.append(item)


list_object=[item for item in lst if isinstance(item,list)]
print(max(list_object,key=len))