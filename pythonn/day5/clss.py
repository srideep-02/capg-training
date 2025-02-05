class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def display_info(self):
        print(f"The car is a {self.brand}, model:{self.model} ")
        
car1= car("suzuki","swift dzire")
car2=car("porsche","911")

car1.display_info()
car2.display_info() 