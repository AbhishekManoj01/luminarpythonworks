from re import findall
f=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\regular_expression\\RE_filework\\data.txt")
content=f.read()
pattern="[0-9]{2}/{1}[0-9]{2}/{1}[0-9]{4}"
dates=findall(pattern,content)
for date in dates:
  print(date)
  