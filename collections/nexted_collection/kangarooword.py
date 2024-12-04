source_word="REGULATE"
target_word="LATE"
# w1={ch:source_word.count(ch) for ch in source_word}
# is_kangaroo=True
# for ch in target_word:

#     if ch in w1.keys() and w1.get(ch)>0:
#         w1[ch]-=1
#     else:
#         is_kangaroo=False
#         break
# print("Kangaroo Word" if is_kangaroo==True else "Not a kangaroo word")

character_count={}
for ch in source_word:
    if ch in character_count:
        character_count[ch]+=1
    else:
        character_count[ch]=1
print(character_count)
iskangaroo_word=True
for ch in target_word:
    if ch in character_count and character_count.get(ch)>0:
        character_count[ch]-=1
    else:
        iskangaroo_word=False
        break
print(iskangaroo_word)