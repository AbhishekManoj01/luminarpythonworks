read_path1="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\students.txt"
fread1=open(read_path1,"r")

read_path2="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\names.txt"
fread2=open(read_path2,"r")

merge_path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\merge.txt"
fmerge=open(merge_path,"w")

contents1=fread1.read()
contents2=fread2.read()

fmerge.write(contents1)
fmerge.write("\n")
fmerge.write(contents2)

fread1.close()
fread2.close()
fmerge.close()