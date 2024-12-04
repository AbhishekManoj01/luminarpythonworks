product={"id":202,"title":"Android Tv","price":45000,"brand":"Samsung"}
product["price"]=55000
product["brand"]="Google"
product["warranty"]="2 years" #if key exist will update value else add new key and value
print("Exist" if "price" in product else "Not exist")
if "offer" in product:
    product["offer"]=10
else:
    product["offer"]=20
print(product)
product["offer"]=product["offer"]+10
print(product)