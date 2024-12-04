def is_factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def test_is_factorial():
   assert is_factorial(-5)==120,"factorial chek failed"

try:
 is_factorial(2)
except Exception as e:
 print(e)
