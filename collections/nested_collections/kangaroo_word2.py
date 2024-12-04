source_word="REGULATE"
target_word="LATE"
ch_count={ch:source_word.count(ch) for ch in source_word}
print(ch_count)
is_kangaroo=True
for ch in target_word:
    if ch in ch_count and ch_count.get(ch)>0:
        ch_count[ch]-=1
    else:
        is_kangaroo=False
        break
print("Kangaroo Word" if is_kangaroo==True else "Not a kangaroo word")
