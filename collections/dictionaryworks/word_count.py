word="hello hai hello hai"
words=word.split(" ")
print(words)
word_count={}
for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)    