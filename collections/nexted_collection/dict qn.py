lst1=["apple","mango","onion","potato"]
lst2=[100,200]
#output={"apple":100,"mango":200,"onion":1,"potato":2}
result={}
for i in range(0,len(lst2)):
    list_one_index=lst1[i]
    list_two_index=lst2[i]

    result[list_one_index]=list_two_index
    balance_element=lst1[len(lst2):]
    for index,element in enumerate(balance_element):
       result[element]=index+1

print(result)   