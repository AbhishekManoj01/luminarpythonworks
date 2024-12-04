orders=["tea","coffee","tea","coffee","gheeroast","plainroast","porotta","tea"]
order_count={}
for item in orders:
    if item in order_count:
        order_count[item]+=1
    else:
        order_count[item]=1
print(order_count)
#print(len(orders))