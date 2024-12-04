def calculator(*args,**kwargs):
    if kwargs.get("operation")=="+":
        return sum(args)
    if kwargs.get("operation")=="*":
        result=1
        for n in args:
            result=result*n
        return result

print(calculator(10,20,30,operation="*"))
print(calculator(10,20,30,operation="+"))