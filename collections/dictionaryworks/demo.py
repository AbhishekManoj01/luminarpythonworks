#syntax:key:value pairs
product={"id":101,"title":"appliance","price":21000,"brand":"lg"}
print(product["id"])
print(product["price"])

#update price of product to 45000
product["price"]=4500
print(product)

# add a new elemnet
product["use by date"]='12-10-26'
print(product)

