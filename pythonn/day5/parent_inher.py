class ug:
    def __init__(self,name,rollno,marks,age):
        self.name=name
        self.__rollno=rollno
        self.age=age
        self.marks=marks
    def get_rollno(self):
        return self.__rollno

class pg(ug):
    def __init__(self, name, rollno, marks, age):
        super().__init__(name, rollno, marks, age)
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.get_rollno())
        print("rno:",self._ug__rollno)
        print("Mars:",self.marks)
        print("Age:",self.age)
p=pg("Srideep",38,100,21)
p.display()
        
        
        