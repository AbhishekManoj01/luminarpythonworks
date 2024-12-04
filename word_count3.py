words=["hello","hai","hello","this","is","this","is","hello"]
#word frequency
word_freq={w:words.count(w)for w in words}
print(word_freq)
#recurive words
recurse=[k for k,v in word_freq.items() if v>1]
print(recurse)
#non recursive
non_recursive=[k for k,v in word_freq.items() if v==1]
print(non_recursive)
#most recursive character
# max_key=max(word_freq, key=word_freq.get)
max_key=max(word_freq, key=lambda k:word_freq.get(k))
# temp=max(word_freq,)
print(max_key)
