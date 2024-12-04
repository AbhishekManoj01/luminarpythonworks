from re import finditer
f=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\regular_expression\\RE_filework\\social_post.txt")
pattern="#\w+"
for line in f:
    words=line.rstrip("\n")
    matcher=finditer(pattern,words)
    for obj in matcher:
        print(obj.group())
    