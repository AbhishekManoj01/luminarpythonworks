f1=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\all_students.txt")
f2=open("C:\\Users\\ASUS\\Desktop\\Pythonworks\\fileinput\\dataset\\failed_students.txt")
set1=set()
set2=set()
for line in f1:
  line=line.rstrip("\n")
  set1.add(line)
for line in f2:
  line=line.rstrip("\n")
  set2.add(line)
passed_stud=set1.difference(set2)
print(passed_stud)