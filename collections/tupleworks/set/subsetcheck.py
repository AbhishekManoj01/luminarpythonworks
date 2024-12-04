text="this is a text to remove duplicate words this text is simple"
words=text.split(" ")
text2="this simple text remove duplicate words"
words2=text2.split(" ")
print(set(words2).issubset(set(words)))
