class Person:
  name=str
  age=int
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display_person_info(self):
   print(self.name,self.age) 
    
class Employee:
   emp_id=int
   salary=int
   def __init__(self,emp_id,salary):
     self.emp_id=emp_id
     self.salary=salary
   def display_Employee_info(self):
    print(self.emp_id,self.salary) 
class Manager(Person,Employee):
  department=str
  def __init__(self,name,age,emp_id,salary,department):
    Person. __init__(self,name,age)
    Employee.__init__(self,emp_id,salary)
    self.department=department
  def display_manager_info(self):
    self.display_person_info()
    self.display_Employee_info()
    print(self.department)
Managerinstance1=Manager("abhi",22,120,2345,"sales")
Managerinstance1.display_manager_info()