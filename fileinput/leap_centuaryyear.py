year_path=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\years.txt","r")
leap_path=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\leap_year.txt","w")
centuary_path=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\centuary_year.txt","w")
for year in year_path:
    year=int(year)
    if year%100==0:
        centuary_path.write(str(year)+"\n")

    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        leap_path.write(str(year)+"\n")

year_path.close()   
leap_path.close()
centuary_path.close()