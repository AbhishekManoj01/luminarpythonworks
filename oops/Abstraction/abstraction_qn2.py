from abc import ABC,abstractmethod
class Editor(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def write(self):
        pass
    @abstractmethod
    def debug(self):
        pass
    @abstractmethod
    def execute(self):
        pass
class vscode:
    def open(self):
        print("open vscode")
    def write(self):
        print("write in vscode")
    def debug(self):
        print("debug")
    def execute(self):
        print("execute")

vscodeinstance=vscode()
vscodeinstance.open()
vscodeinstance.write()
vscodeinstance.debug()
vscodeinstance.execute()
