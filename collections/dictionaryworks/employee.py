employee={"eid":101,"name":"Abhishek","salary":60000,"department":"HR","experience":6}
employee["contact"]=987653210
print(employee)
employee["salary"]=employee["salary"]+10000 if employee["experience"]>5 else employee["salary"]+5000
employee["role"]="SDE" if employee["experience"]>5 else "JDE"
print(employee)
