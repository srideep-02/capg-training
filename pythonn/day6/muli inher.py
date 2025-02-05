class man:
    def man(self):
        print("Iam man")
        
class women:
    def women(self):
        print("Iam women")
        
class person(man,women):
    pass

obj=man()
obj.man()
obj1=person()
obj1.man()
obj1.women()
obj=obj1
obj.man()
obj.women()
