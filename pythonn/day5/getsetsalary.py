class employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
    def set_salary(self,salary):
        self._salary=salary
        
    def get_salary(self):
        return self._salary
    
emp = employee("Srideep",10000)
print("Salary before update",emp.get_salary())
emp.set_salary(5000)
print("Salary after update",emp.get_salary())