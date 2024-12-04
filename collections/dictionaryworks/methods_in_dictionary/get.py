#get method (if we use get() we cannot get an error msg if the specified field in not in dictionary it return a none msg)

employee={"id":100,"name":"hari","department":"hr","age":32,"salary":25500}
print(employee.get("salary"))
