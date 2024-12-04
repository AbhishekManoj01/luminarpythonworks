class Person:
  name:str
  age:int
  def __init__(self,name,age):
    self.name=name
    self.age=age
  @property
  def get_age(self):
    print(self.age)
person_instance=Person("hasi",22)
person_instance.get_age
