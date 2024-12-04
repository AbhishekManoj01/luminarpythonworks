# for abstraction 
from abc import ABC,abstractmethod
class Bike(ABC):
    @abstractmethod
    def start(self):
     pass
    @abstractmethod
    def accelerate(self):
     pass
    @abstractmethod
    def stop(self):
      pass

class Hunter(Bike):
  def start(self):
    print("hunter start")
  def accelerate(self):
     print("hunter accelerate")
  def stop(self):
     print("hunter stop method")

hunterinstance=Hunter()
hunterinstance.start()
hunterinstance.accelerate()
hunterinstance.stop()