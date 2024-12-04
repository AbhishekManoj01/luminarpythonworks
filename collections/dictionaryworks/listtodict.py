lst1=["apple","mango","onion","potatto"]
lst2=[100,200]
dict1={lst1[i]:lst2[i] for i in range(len(lst2))}
balance_elements=lst1[len(lst2):]
print(balance_elements)
# dict1={lst1[index]:index+1 for index,element in enumerate(balance_elements)}
for index,element in enumerate(balance_elements):
    dict1[element]=index+1
print(dict1)

# dict2={}
# for i in range(len(lst2)):
#     dict2[lst1[i]]=lst2[i]
# print(dict2)

# i=0
# v1=1
# dict1={}
# while(i<len(lst2)):
#     dict1[lst1[i]]=lst2[i]
#     i+=1
# while(i<len(lst1)):
#     dict1[lst1[i]]=v1
#     i+=1
#     v1+=1
print(dict1)