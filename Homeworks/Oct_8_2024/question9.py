path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\students.txt"
fread=open(path,"r")

for line_num,line in enumerate(fread,start=1):
    if line_num%2==0:
        print(line.strip("\n"))
fread.close()