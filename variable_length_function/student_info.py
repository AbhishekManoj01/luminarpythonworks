def student_info(*args,**kwargs):
    if kwargs.get("operation")=="avg":
        avag=sum(args)/len(args)
        return avag
    if kwargs.get("operation")=="total":
        total=sum(args)
        return total



print(student_info(45,43,44,operation="avg"))
print(student_info(45,43,44,operation="total"))