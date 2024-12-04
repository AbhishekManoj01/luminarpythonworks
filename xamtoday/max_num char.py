text = "this is a simple question return word with maximum number of characters" 

list_text=text.split(" ")
word=max(list_text,key=lambda x:len(x))
print(word)