# def smart_sub(num1,num2):
#  if num1<num2:
#     (num1,num2)=(num2,num1)
#  return(num1-num2)
    
# def smart_div(num1,num2):
#   if num1<num2:
#     (num1,num2)=(num2,num1)
#   return(num1/num2)

# print(smart_sub(10,2))
# print(smart_sub(2,10))


   #DECORATORS
def swap_dec(fn):
  def wrapper(n1,n2):
    if n2>n1:
      (n1,n2)=(n2,n1)
    return fn(n1,n2)
  return wrapper

@swap_dec
def smart_sub(num1,num2):
 return(num1-num2)
@swap_dec
def smart_div(num1,num2):
  return(num1/num2)
  

print(smart_sub(10,2))
print(smart_sub(2,10))
