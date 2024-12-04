product={"id":101,"title":"appliance","price":21000,"brand":"lg","offer":5}
if "offer" in product:
    product["offer"]=10
else:
    product["offer"]=20
print(product)