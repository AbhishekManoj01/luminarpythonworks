
# st={1,2,1,3,4} does not support duplicates
# st ={1,2,"hello",3,4,"hai",True} insertion order does not preserved
# mutable
# print(type(st))
# print(st)
# st[0] Indexing does not support

colors={"red","green","blue"}
colors.add("yellow")
# print(colors)
st1={1,2,3,10,20}
st2={1,2,3,4,5}
st1.update(st2)
# print(st1)
# print(st2.issuperset(st1))
# print(st2.symmetric_difference(st1))

text="this is a test to remove duplicate words this test is simple"
text2="this simple test remove duplicate words"
words=text.split(" ")
words2=text2.split(" ")
print(set(words2).issubset(set(words)))
