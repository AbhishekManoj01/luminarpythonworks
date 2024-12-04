#    method overloading:same method name and differnt number of parameters

#    due to *args pythod does not support method overloading 

class Operation:
    def add(self,num1,num2):          #def add(*args)
        print(num1+num2)               #print(sum(args))
    def add(self,num1,num2,num3):
        print(num1+num2+num3)

obj=Operation()
obj.add(10,20,30)
#obj.add(20,30)