from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def display(self):
        pass
    def show(self):
        print("Concrete method")    

class son(Father):
    def display(self):
        print("son")
    def show(self):
       #  super().show()
        print("show son")  

class daughter(Father):
    def display(self):
        print("daughter is implementing the abstact class")
 

obj=daughter()
obj.display()
obj2=son()
obj2.display()
obj2.show()

