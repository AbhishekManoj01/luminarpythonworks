text="this is a simple programming question to find word with to maximum number of characters"
words=text.split(" ")
print(max(words,key=lambda word:len(word)))
# temp=sorted(words,key=lambda word:len(word),reverse=True)
print(sorted(words,key=lambda word:len(word),reverse=True))
print(max(words,key=lambda word:words.count(word)))