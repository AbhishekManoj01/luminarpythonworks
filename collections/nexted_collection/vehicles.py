cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]
#print count of vehicles
print("TOTAL NO OF VEHICLES:",len(cars))
#print available colours of baleno
baleno_clrs=[c.get("colors") for c in cars if c.get("name")=="baleno"]
print(baleno_clrs[0])
#print all brands 
nexa_vehicles={c.get("brand") for c in cars }
print(nexa_vehicles)
#print car names available in amt transmission
amt_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(amt_cars)
#cars available in blue colour
blue_cars=[c.get("name") for c in cars if "blue" in c.get("colors") ]
print(blue_cars)
#print all transmission type
transmission_type={t for c in cars for t in c.get("transmissions")}
print(transmission_type)
#print all colors
colours={colour for c in cars for colour in c.get("colors")}
print(colours)

#count of colours
popular_colors=[color for c in cars for color in c.get("colors")]
popular_color={color:popular_colors.count(color) for color in popular_colors}
print(popular_color)
colors=max(popular_color,key=lambda c:popular_color.get(c))
print(colors)

#expensive
max_price=max(cars,key=lambda p:p.get("price"))
print(max_price.get("name")) 

#minimum expensive
min_price=min(cars,key=lambda p:p.get("price"))
print(min_price.get("name"))

#sorting
sorted_list=sorted(cars,key=lambda c:c.get("price"))
# sorted_list_names=[[entry.get("name"),entry.get("price")] for entry in sorted_list]
sorted_dict={entry.get("name"):entry.get("price") for entry in sorted_list}
print(sorted_dict)
# two values in list
sorted_car_name={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_list}
print(sorted_car_name)