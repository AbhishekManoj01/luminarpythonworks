text="hello hai hello hai hello hai hello"
words=text.split(" ")
print(words)
freq_count={word:words.count(word) for word in words}
print(freq_count)