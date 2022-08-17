from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def doSomething(self):
        return NotImplemented
    
    def callSomething(self):
        self.doSomething()


class Mixin:
    def doSomething(self):
        print("I'm mixin.")


# class Concrete(Abstract, Mixin): # これはだめ
class Concrete(Mixin, Abstract):
    def main(self):
        self.callSomething()


c = Concrete()
c.main()
