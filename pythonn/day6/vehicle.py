class shape:
    def area(self):
        pass
    
class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
         
    def area(self):
        return 3.14*self.radius ** 2
    
class Square(shape):
    def __init__(self,side):
        self.side=side
         
    def area(self):
        return self.side**2
s=Square(5)
print("Area of rectangle is :",s.area())

c=Circle(5)
print("Area of circle is : ",c.area())
