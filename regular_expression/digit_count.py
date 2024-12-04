from re import finditer
text="I have 3 cars,2 bike and 1 cycle"
pattern="[a-zA-Z0-9]"#"[a-zA-Z]" #"[0-9]"
matcher=finditer(pattern,text)
for obj in matcher:
  print(obj.start(),obj.group())