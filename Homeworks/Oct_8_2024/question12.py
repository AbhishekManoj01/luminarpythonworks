fread=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\students.txt")
ch_list=[]
for line in fread:
    line=line.strip("\n")
    for ch in line:
        ch_list.append(ch)

ch_count={ch:ch_list.count(ch) for ch in ch_list}
print(ch_count)
fread.close()