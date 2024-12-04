path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\duplicate_lines.txt"
fread=open(path)

dup=[]

for w in fread:
    w=w.rstrip("\n")
    if w not in dup:
        dup.append(w)
fread.close()

fwrite=open(path,"w")
for w in dup:
    fwrite.write(w+"\n")
fwrite.close()

    