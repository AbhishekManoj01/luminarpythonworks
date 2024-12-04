from re import finditer
text="abaabbaabbbaaab"
#pattern="a{2}" #for finding aa in text
pattern="a*"#* any number including 0
pattern="a{1,3}"#min 1a max 3a
pattern="[a-z]{2}"
matcher=finditer(pattern,text)
for obj in matcher:
    print(obj.start(),obj.group())