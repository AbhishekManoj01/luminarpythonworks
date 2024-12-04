class Animal:
    name:str
    species:str
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def __str__(self):
        return self.name
class Lion(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)
    def sound(self):
        print("roar")




class Cat:
    def __init__(self,name,species):
        super().__init__(name,species)
    def sound(self):
        print("meow")

lion_instance1=Lion("lion","carnivorous")
print(lion_instance1.sound())