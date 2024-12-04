from json import load
f=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\employee.json","r")
data=load(f)
for emp in data:
    print(emp)