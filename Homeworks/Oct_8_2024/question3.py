path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\question.txt"
fread=open(path,"r")
lst=[]
for line in fread:
    line=line.strip("\n")
    words=line.split(" ")
    lst.extend(words)
print(len(lst))
fread.close()