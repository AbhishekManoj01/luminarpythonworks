f=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\years.txt","w")
for year in range(1000,2000):
    f.write(str(year)+"\n")
f.close()