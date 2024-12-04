words=["hello","hai","apple"]
# def get_length(word):
#     return len(word)
# print(max(words,key=get_length))

print(max(words,key=lambda word:len(word)))