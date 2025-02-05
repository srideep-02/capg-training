from abc import ABC, abstractmethod
from typing import List

# Step 1: Define Employee interface using Abstract Base Class (ABC)
class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        pass


# Step 2: Create concrete classes for different types of employees

class Manager(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role= "manager"

    def work(self) -> str:
        return f"{self.name} is managing the team."

    def get_salary(self) -> float:
        return self.salary


class Developer(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role= "developer"


    def work(self) -> str:
        return f"{self.name} is writing code."

    def get_salary(self) -> float:
        return self.salary


class Intern(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role= "intern"


    def work(self) -> str:
        return f"{self.name} is learning and assisting."

    def get_salary(self) -> float:
        return self.salary
    
class Security(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        self.role= "Security staff"

    def work(self) -> str:
        return f"{self.name} is Securing the assets."

    def get_salary(self) -> float:
        return self.salary


# Step 3: Define Department class that manages Employees

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired.")

    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")
        
    def promote(self, employee: Employee) -> None:
        if self.role == "intern":
            self.employees.remove(employee)
            print(f"{employee.name} has been removed from employee list.")
            self.employees.append(Developer(employee.name,employee.salary+10000))
            print(f"{employee.name} has been promoted to developer")
        elif self.role == "developer":
            self.employees.remove(employee)
            print(f"{employee.name} has been removed from employee list.")
            self.employees.append(Manager(employee.name,employee.salary+10000))
            print(f"{employee.name} has been promoted to manager")
        elif self.role == "manager":
            self.employees.remove(employee)
            print(f"{employee.name} has the highest level as manager")
        
    def demote(self, employee: Employee) -> None:
        if self.role == "manager":
            self.employees.remove(employee)
            print(f"{employee.name} has been removed from employee list.")
            self.employees.append(Developer(employee.name,employee.salary+10000))
            print(f"{employee.name} has been demoted to developer")
        elif self.role == "developer":
            self.employees.remove(employee)
            print(f"{employee.name} has been removed from employee list.")
            self.employees.append(Intern(employee.name,employee.salary+10000))
            print(f"{employee.name} has been promoted to manager")
        elif self.role == "intern":
            self.employees.remove(employee)
            print(f"{employee.name} has the lowest level as intern")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")


# Step 4: Create department and add employees

# Create employees
manager = Manager("Alice", 80000)
developer = Developer("Bob", 60000)
intern = Intern("Charlie", 20000)
securitystaff=Security("Ram",5000)

# Create a department and hire employees
it_department = Department("IT")

it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(securitystaff)
it_department.fire(intern)
# Show employee details
it_department.show_employee_details()

# Total salary in the department
total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")