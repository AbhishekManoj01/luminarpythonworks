products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000},
    {"id":6,"title":"iphone16proplus","brand":"apple","price":150000},
    {"id":8,"title":"nokia105","brand":"nokia","price":900}

]

# total number of mobiles
print(len(products))

# print mobile titles
product_titles=[m.get("title") for m in products]
print(product_titles)

# print samsung mobiles
samsung_mobiles=[m.get("title") for m in products if m.get("brand")=="samsung"]
print(samsung_mobiles)
print(len(samsung_mobiles))

#print samsung count
price_gt_20k=[m.get("title")for m in products if m.get("price")>20000]
print(price_gt_20k)

# expensive=max(products,key=lambda m:m["price"])
# highest=expensive.get("price")
# costly_mobiles=[m.get("title")for m in products if m.get("price")==highest]
# print(costly_mobiles)
# print(min(products,key=lambda m:m["price"])["title"])

# list1=[product['title'] for product in products if product['price'] == max(p['price'] for p in products)]
list2=[product.get("title") for product in products if product["price"]==max(p["price"]for p in products)]
print(list2)

all_brands=[p.get("brand")for p in products]
print(all_brands)
brand_count={b:all_brands.count(b)for b in all_brands}
print(brand_count)


# brand_count1=[for p in range(len(products))]


