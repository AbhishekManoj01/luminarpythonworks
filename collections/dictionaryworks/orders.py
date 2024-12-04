orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]
dict={}
# dict[item]=[dict[item]+1 if item in dict else 1 for item in orders]

dict1={item:orders.count(item) for item in orders}
print(dict1)