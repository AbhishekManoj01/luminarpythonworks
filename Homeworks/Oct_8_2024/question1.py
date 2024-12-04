path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\user_input_file.txt"

user_input=input("Enter the input :")
fwrite=open(path,"w")
fwrite.write(user_input)
fwrite.close()

fread=open(path,"r")

fread=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\user_input_file.txt","r")
print(fread.read())
# for line in fread:
#     print(line.strip("\n"))
fread.close()