text="silent"
text1="listen"
check=True
for ch in text1:
    if ch not in text:
        check=False
        break
if(check==True):
    print("anagram")       
else:
    print("not anagram")
 