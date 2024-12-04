from re import finditer
text="fatcatrunveryfast"
matcher=finditer("at",text)#[(satrt,group),(),()]
for obj in matcher:
    print(obj.start(),obj.group())