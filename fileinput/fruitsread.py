
f=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\fruits.txt","r")
lst=[]
for line in f:
    lst.append(line.rstrip("\n"))
print(lst)