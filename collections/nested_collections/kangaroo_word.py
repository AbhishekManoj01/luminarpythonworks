source_word="REGULATE"
target_word="LATE"
w1={ch:source_word.count(ch) for ch in source_word}
is_kangaroo=True
for i in range(len(target_word)):
    ch=target_word[i]
    if ch in w1.keys() and w1.get(ch)>0:
        w1[ch]-=1
        is_kangaroo=True
    else:
        is_kangaroo=False
        break
print("Kangaroo Word" if is_kangaroo==True else "Not a kangaroo word")
