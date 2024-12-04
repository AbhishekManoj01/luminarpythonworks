# txt1=input("enter the string 1")
# txt2=input("enter the string 2")
# len1=len(txt1)
# len2=len(txt2)
# result=""
# #if len1==len2:
# for i in range(0,len1):
#         result=result+txt1[i]+txt2[i]
# print(result)
    

txt1=input("enter the string 1")
txt2=input("enter the string 2")
smallest_txt=txt1 if txt1<txt2 else txt2
largest_txt=txt1 if txt1>txt2 else txt2
result=""
for i in range(0,len(smallest_txt)):
    result=result+txt1[i]+txt2[i]
balace_txt=largest_txt[len(smallest_txt):]
result=result+balace_txt
print(result)