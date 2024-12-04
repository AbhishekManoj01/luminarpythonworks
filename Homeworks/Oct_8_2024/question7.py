path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\question.txt"
fread=open(path,"r")
for line in fread:
    line=line.strip("\n")
    reverse=line[::-1]
    print(reverse)
fread.close()