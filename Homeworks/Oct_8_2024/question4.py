path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\all_students.txt"
fread=open(path,"r")
all_lines=fread.readlines()
# lines=[line.strip("\n") for line in fread]
print(len(all_lines))
fread.close()