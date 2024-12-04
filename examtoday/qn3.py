def most_frequent_word(txt):
    words=text.split(" ")
    word=max(words,key=lambda w:words.count(w))
    return word

text=input("Enter the text:").casefold()
freq_word=most_frequent_word(text)

print(freq_word)