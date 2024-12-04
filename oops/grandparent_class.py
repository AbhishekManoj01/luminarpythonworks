class Grandparent:
  def m1(self):
    print("grand parent class m1 method")
class Parent:
   def m2(self):   
     print("parent classs m2 method")
class Child(Parent,Grandparent):
   def m3(self):
     print("child class m3 method")

child_insstance=Child()
child_insstance.m3()
child_insstance.m2()
child_insstance.m1()