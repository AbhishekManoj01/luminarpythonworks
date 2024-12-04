def swap_dec(fn):
    def wrapper(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper
def round_dec(fn):
   def wrapper(num1,num2):
      num1=round(num1)
      num2=round(num2)
      return fn(num1,num2)
   return wrapper
@round_dec
@swap_dec
def add_number(num1,num2):
  return(num1+num2)
@round_dec
@swap_dec
def substraction(num1,num2):
 return(num1-num2)
@round_dec
@swap_dec
def division(num1,num2):
 return(num1/num2)
print(substraction(2.4,10.8))