path="C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\blank_space.txt"
fread=open(path)
contents=fread.readlines()

lst=[w.rstrip("\n") for w in contents if w!="\n"]
fread.close()

fwrite=open(path,"w")
for word in lst:
    fwrite.write(word+"\n")