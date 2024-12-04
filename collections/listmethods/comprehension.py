
# #normal method
# # arr=[2,3,4,5,6,7]
# # cubes=[]
# # for num in arr:
# #     cubes.append(num**3)
# # print(cubes)

# #list comprehension
# arr=[2,3,4,5,6,7]
# add_five=[num+2 for num in arr]
# squares=[num**2 for num in arr]
# # print(squares)
# # print(add_five)
# num_gt_five=[num for num in arr if num>5]
# num_ls_five=[num for num in arr if num<5]
# odd_numbers=[num for num in arr if num%2!=0]
# even_numbers=[num for num in arr if num%2==0]
# new_list=[num+1 if num>5 else num-1 for num in arr ]
# print(new_list)
# print(even_numbers)
# print(odd_numbers)
# print(num_ls_five)
# print(num_gt_five)
# for i in add_five:
#     print(i,end=" ")
text=["apple","iphone","orange","potatto"]
print(text)
# vow=["a","e","i","o","u"]
# words=[ch for ch in text if ch[0] in vow ]
# print(words)
ch_count=max([len(ch) for ch in text])
long_word=[ch for ch in text if len(ch)==ch_count]
print(long_word)