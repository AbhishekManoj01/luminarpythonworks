products=[
    {"id":1,"title":"s23ultra","brand":"samsung","price":78000},
    {"id":2,"title":"a17","brand":"samsung","price":18000},
    {"id":3,"title":"m50","brand":"samsung","price":16000},
    {"id":4,"title":"pocom3","brand":"poco","price":15000},
    {"id":7,"title":"vivov50","brand":"vivo","price":25000},
    {"id":5,"title":"oppof19pro","brand":"oppo","price":27000},
    {"id":6,"title":"iphone16pro","brand":"apple","price":150000}, 
    {"id":9,"title":"iphone16pro plus","brand":"apple","price":150000}, 
    {"id":8,"title":"nokia105","brand":"nokia","price":900}

]

# total number of mobiles
print(len(products))
# print mobile titles
mobile_titles=[m.get("title")for m in products]
print(mobile_titles)
# print samsung mobiles
sam_mobiles=[m.get("title")for m in products if m.get("brand")=="samsung"]
print(sam_mobiles)
#print costly product
costly_mobile=max(products,key=lambda d:d.get("price"))
max_price=costly_mobile.get("price")
costly_mobiles=[m.get("title")for m in products if m.get("price")==max_price]
print(costly_mobiles)
#samsung mobile count
print(m for m in products if m.get("brand")=="samsung")
print(len(sam_mobiles))