class des:
    def __init__(self,name):
        self.name=name
        print(f"hi{self.name}")
    def __del__(self):
        print(f"bye{self.name}")
obj=des("john")
del obj
        