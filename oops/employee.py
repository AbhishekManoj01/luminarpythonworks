class Employee:
    name:str
    age:int
    course:str
    def set_student(self,name,age,course):
      self.name=name
      self.age=age
      self.course=course
    def display(self):
     print(self.name,self.age,self.course)
employee_instance1=Employee()
employee_instance1.set_student("abhi",22,"django")
employee_instance1.display() 