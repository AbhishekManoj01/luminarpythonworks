text="this is a simple proogrammoing  question to find word with a maximum number of characters"
words=text.split(" ")
def get_count(w):
 return words.count(w)
freq_word=max(words,key=get_count)
print(freq_word)