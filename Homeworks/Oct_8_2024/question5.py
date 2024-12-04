read_path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\all_students.txt"
fread=open(read_path,"r")

write_path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\all_students_copy.txt"
fwrite=open(write_path,"w")

for line in fread:
    fwrite.write(line)
 
fread.close()
fwrite.close()
 