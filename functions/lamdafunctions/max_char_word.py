text="this is a simple proogrammoing  question to find word with a maximum number of characters"
words=text.split(" ")
print(max(words,key=lambda word:len(word)))