class Editors:
    name:str
    vendor:str
    def __init__(self,name,vendor):
     self.name=name
     self.vendor=vendor
    def __str__(self):
     return self.name
editor_instance1=Editors("pycharm","jebrains")
editor_instance2=Editors("intellij","jetbrains")
editor_instance3=Editors("vscode","microsoft")
print(editor_instance2)