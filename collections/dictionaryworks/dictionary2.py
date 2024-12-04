employee={"eid":102,"name":"sebin","salary":20000,"dapartment":"sales","experience":3}
employee["contact"]=7345678910
print(employee)
if employee["experience"]>5:
    employee["salary"]+=100000
else:
    employee["salary"]+=5000
print(employee)

if employee["experience"]>5:
    employee["role"]="SDE" 
else:
    employee["role"]="JDE"
print(employee)
