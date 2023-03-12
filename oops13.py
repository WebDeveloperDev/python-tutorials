class Employee:
    Country="INDIA"
    _protec="protected string"
    __private="this is private"
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"Name is {self.name} . Salary is {self.salary} and role is {self.role}"
    def __add__(self, other):
        return self.salary+other.salary
    def __truediv__(self, other):
        return self.salary/other.salary
    def __repr__(self):
        return f"Employee('{self.name}' , {self.salary},'{self.role}')"
    def __str__(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is {self.role}"
harry=Employee("Harry",433,"programmer")
rohan=Employee("Rohan",33,"driver")
print(harry+rohan)
print(harry/rohan)
print(repr(rohan))
print(harry )