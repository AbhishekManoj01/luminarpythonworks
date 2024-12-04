from re import finditer
text="I have 3 cars,2 bike- and 1 Cycle"
#pattern="\w"  for alphanumeric     
#pattern= "\d" for digits[0-9]
#pattern="\D" for excluding digits
#pattern="\W" for special characters #[^a-zA-Z0-9]
#pattern="\s" #for space
pattern="\S" #for exclude space
matcher=finditer(pattern,text)
for obj in matcher:
    print(obj.start(),obj.group())