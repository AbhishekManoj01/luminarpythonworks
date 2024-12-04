

text = "this is a simple python program that print most recursive word . this program is simple" 
words=text.split(" ")
word=max(words,key=lambda w:words.count(w))
print(word)
