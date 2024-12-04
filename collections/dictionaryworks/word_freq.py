text="ABBBCDCCAA"
# freq={ch:text.count(ch)for ch in text}
# print(freq)

# temp=[k for k,v in freq.items() if v==1]
min_value=min(text,key=lambda f:text.count(f))
print(min_value)
# print(temp)
# for k,v in freq.items():
#     if v==1:
#         print(k)