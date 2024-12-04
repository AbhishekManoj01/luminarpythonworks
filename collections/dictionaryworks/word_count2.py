text="ABCCABB"
# recurse={}
# for ch in text:
#     if ch in recurse:
#         if recurse[ch]==1:
#             break
#         recurse[ch]+=1
#     else:
#          recurse[ch]=1
# print("First Recursive character")
# print(ch)

print("Character count")
ch_count={ch: text.count(ch) for ch in text }
for k in ch_count.keys():
    if ch_count[k]>1:
        print(k)

