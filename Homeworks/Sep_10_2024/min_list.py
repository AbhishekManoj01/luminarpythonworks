expenses=[12000,13000,14000,11000,12000]
min_list=expenses[0]
for i in expenses:
    if min_list>i:
        min_list=i
print(min_list)