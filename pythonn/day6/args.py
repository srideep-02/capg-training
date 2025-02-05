class Example:
    def __init__(self,name):
        print(f"First constructer :Heello{name}")
    def __init__(self,age):
        print(f"second constructer age is{age}")
obj=Example(25)


class Example:
    def __init__(self,*args):
        if len(args)==1:
            print(f"Hello {args[0]}")
        elif len(args)==2:
            print(f"Hello {args[0]},you are {args[1]} years old")
        elif len(args)==3:
            print(f"Hello {args[0]},you are {args[1]} years old on {args[2]}")
obj=Example(22,4,5)

class Example:
    def __init__(self,student_name,**kwargs):
        self.student_name=student_name
        if 'name' in kwargs and 'age' in kwargs:
            print(f"Hello {kwargs['name']}, you are {kwargs['age']} years old")
        elif 'name' in kwargs:
            print(f"Hello {kwargs['name']}")
        self.xfield=kwargs['name']
# obj=Example(name='alice')
obj1=Example('name'=alice,'age'=2)
print(obj1.student_name)