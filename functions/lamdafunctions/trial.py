text="this is a simple proogrammoing  question to find word with a maximum number of character"
words=text.split(" ")
print(max(words,key=lambda word:words.count(word)))