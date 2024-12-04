# child class has to acess attributes and methods of a parent class ie inheritance
#syt :in child class name give inherant class name in parantesis

class Parent:
    def vehicle(self):
        print("parent class ertiga vehicle")
class Child(Parent):
    pass
child_instance1=Child() 
child_instance1.vehicle()