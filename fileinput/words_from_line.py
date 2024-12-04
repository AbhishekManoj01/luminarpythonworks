f=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\text","r")
words=[]
for line in f:
   line=line.rstrip("\n")
   all_words=line.split(" ")
   for w in all_words:
    words.append(w)
print(words)

word_count={w:words.count(w) for w in words}

nested_words_count=[[v,k] for k,v in word_count.items()]
print(sorted(nested_words_count,reverse=True))