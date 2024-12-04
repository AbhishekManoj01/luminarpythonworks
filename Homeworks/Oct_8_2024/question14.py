path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\question1.txt"
path1="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\question2.txt"
fread=open(path,"r")
contents=fread.readlines()
fread.close()

fwrite=open(path1,"w")
for line in contents:
    line=line.rstrip("\n")
    line=line.replace("program","welcome")
    fwrite.write(line+"\n")

fwrite.close()
    
 

