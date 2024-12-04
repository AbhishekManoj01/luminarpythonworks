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
# print(f"Total no of vehicles:{len(cars)}")
#print available colors of baleno
baleno_colors=[c.get("colors") for c in cars if c.get("name")=="baleno"]#[0]
# print(baleno_colors[0])

#print all amt transmission vehicles
amt_vehicles=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(amt_vehicles)

# max_price=max(cars,key=lambda p:p.get("price"))
all_brands=set([c.get("brand") for c in cars])
all_brands1={c.get("brand") for c in cars}
# print(all_brands)

#print all blue cars
blue_cars=[c.get("name") for c in cars if "blue" in c.get("colors")]
# print(blue_cars)

#expensive car
expensive=max(cars,key=lambda c:c.get("price"))
# print(expensive)

#print all transmission
trans_types=[c1 for c in cars for c1 in c.get("transmissions")]
# trans_types1={c1 for c in cars for c1 in c.get("transmissions")}
print(set(trans_types))
# print(trans_types1)

all_colors={color for c in cars for color in c.get("colors")}
print(all_colors)

#popular color
total_colors=[color for car in cars for color in car.get("colors")]
total_color_count={color:total_colors.count(color) for color in total_colors}
print(total_color_count)
popular_color=max(total_color_count,key=lambda color:total_color_count.get(color))
print(popular_color)

#expensive
max_price=max(cars,key=lambda car:car.get("price"))
print("Most expensive :",max_price.get("name"))

#minimum expensive
min_price=min(cars,key=lambda car:car.get("price"))
print("Least expensive :",min_price.get("name"))

#sorting
sorted_list=sorted(cars,key=lambda car:car.get("price"))
# sorted_list_names=[[entry.get("name"),entry.get("price")] for entry in sorted_list]
# print(sorted_list_names)
sorted_dict={car.get("name"):[car.get("price"),car.get("transmissions")] for car in sorted_list}
print(sorted_dict)
# sorted_car_names=[car.get("name") for car in sorted_list]
# print(sorted_car_names)
