path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\students.txt"
fappend=open(path,"a")

user_input=input("Enter more names :")
fappend.write(user_input+"\n")
fappend.close()

fread=open(path,"r")
print(fread.read())
# for line in fread:
#     print(line.strip("\n"))  
fread.close()
    
