products={"pen":10,"book":80,"pencil":45,"marker":50}
abv_50={item:price for item,price in products.items() if price>50}
print(abv_50)