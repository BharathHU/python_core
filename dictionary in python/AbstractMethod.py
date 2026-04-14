from abc import ABC,abstractmethod
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
class PetrolEngine(Engine):
    def start(self):
        print("Petrol Engine is start")
    def stop(self):
        print("Petrol Engine is Stop")
class DieselEngine(Engine):
    def start(self):
        print("Diesel Engine is start")
    def stop(self):
        print("Diesel Engine is Stop")
class Car:
    def __init__(self,Engine):
        self.Engine=Engine
    def startEngine(self):
        self.Engine.start()
    def stopEngine(self):
        self.Engine.stop()
p=PetrolEngine()
d=DieselEngine()
c=Car(d)
c.startEngine()
c.stopEngine()
c=Car(p)
c.startEngine()
c.stopEngine()