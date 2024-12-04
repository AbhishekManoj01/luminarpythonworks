text="ABAABBC"
#most recursive character
print(max(text,key=lambda ch:text.count(ch)))
#least recursive
print(min(text,key=lambda ch:text.count(ch)))
#non recursive
# dict1={}
# for ch in text:
#     if ch not in dict1:
#         dict1[ch]=1
#     else:
#         if dict1[ch]==1:
#             print(dict1[ch])
#             break
# print(dict1)

dict1={ch:text.count(ch) for ch in text if text.count(ch)==1}
print(dict1)