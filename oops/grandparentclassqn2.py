class Grandparent:
  def m(self):
    print("grand parent class m method")
class Parent:
   def m(self):   
     print("parent classs m method")
class Child(Parent,Grandparent):
   def m3(self):
     print("child class m3 method")

child_insstance=Child()
child_insstance.m3()
child_insstance.m()