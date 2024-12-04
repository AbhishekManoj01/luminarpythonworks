from json import load
f=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\countries.json",encoding="UTF-8")
data=load(f)
                 # number of countries
#print(len(data))
                 # all country name
all_country_name=[country.get("name") for country in data]
#print(all_country_name)
                 #print all regions
all_regions=[countries.get("region") for countries in data]
#print(set(all_regions))
 
region_count={reg:all_regions.count(reg) for reg in all_regions}
#print(region_count)
        #max count
max_count=max(region_count,key=lambda k:region_count.get(k))
#print(max_count)
        #capital of a specific country
country_capital=[country.get("capital") for country in data if country.get("name")=="India"]
#print(country_capital)
        #countries with most number of borders
country_bordrder_count={country.get("name"):len(country.get("borders",[]))for country in data }
#print(country_bordrder_count)
max_l=max(country_bordrder_count,key=lambda c:country_bordrder_count.get(c))
#or#   max_border_count=max(data,key=lambda country:len(country.get("borders",[]))).get("name")
#print(max_l)
    #most popualted country
populated_list={country.get("name"):country.get("population") for country in data}
populated_country=max(populated_list,key=lambda c:populated_list.get(c))
#print(populated_country)


alpha_3_code=[country.get("borders") for country in data if country.get("name")=="China"][0]
#print(alpha_3_code)
for code in  alpha_3_code:
    for country in data:
        if country.get("alpha3Code")==code:
            print(country.get("name"))