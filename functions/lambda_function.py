# #adding two numbers
# add=lambda n1,n2:n1+n2

# print(add(4,5))

# #difference of two number
# sub=lambda n1,n2:n1-n2

# print(sub(9,6))

# #cube of number
# cube=lambda n1:n1**3
# print(cube(3))

# #largest word
# largest_word=lambda str1,str2:str1 if len(str1)> len(str2) else str2
# print(largest_word("hai","hello"))

# #smallest word
# smallest_word=lambda str1,str2:str1 if len(str1)< len(str2) else str2
# print(smallest_word("hai","hello"))

# #smart sub
# smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
# print(smart_sub(2,10))

# words=["hello","hai","morning","test"]

# # get_length=lambda str1:len(str1)
# # print(max(words,key=get_length))


# print(max(words,key=lambda str1:len(str1)))
words=["hello","hai","morning","test","apple"]

srt_words=sorted(words,key=lambda word:len(word),reverse=True)
print(srt_words)