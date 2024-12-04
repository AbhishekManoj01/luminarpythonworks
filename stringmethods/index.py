text="hello world"
print(text.index("o"))



text="vishal@gmail.com"
var=(text.index("@"))
print(text[0:var])

text="hellopython"
o_index=text.index("o")
rev=(text[o_index-1::-1])
bal=(text[o_index::])
str=rev+bal
print(str)