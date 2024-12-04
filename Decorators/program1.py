def swap_decorator(fn):
    def wrapper(n1,n2):
        if n1<n2:
            n1,n2=n2,n1
        return fn(n1,n2)
    return wrapper

def round_fn(fn):
    def wrapper(n1,n2):
        n1=round(n1)
        n2=round(n2)
        return fn(n1,n2)
    return wrapper

@round_fn
@swap_decorator
def add_number(num1,num2):
    return num1+num2

@round_fn
@swap_decorator
def subtraction(num1,num2):
    return num1-num2

@round_fn
@swap_decorator
def division(num1,num2):
    return num1/num2
    
print(add_number(2.3,10.4))
