path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\question.txt"
fread=open(path,"r")
lst=[]
for line in fread:
    line=line.strip("\n")
    words=line.split(" ")
    lst.extend(words)
long_word=max(lst,key=lambda w:len(w))
print(long_word)