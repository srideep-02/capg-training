class Employee:
    
    __tax = 0.1
    __pf = 0.02
    __insurance = 0.01
    __bonus = 0.1
    __hra = 0.1
    __da = 0.05
    def _init_(self,employee_id,name,age,depart,salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.depart = depart
        self.salary = salary
        
    def gross(self):
        return round(self.salary * ( 1+ self._hra + self.bonus + self._da),2)
    
    def deductions(self):
        return round(self.salary * (self._pf + self.insurance + self._tax),2)
    
    def net_salary(self):
        return round(self.gross() - self.deductions(),2)
    
    
e1 = Employee(1,"sri",'23',"Devop",50000)
print("Gross Salary:",e1.gross())
print("Deductions:",e1.deductions())
print("Net Salary:",e1.net_salary())