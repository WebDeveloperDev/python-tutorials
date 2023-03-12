class Employee:
    Country="INDIA"
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"Name is {self.name} . Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_country(cls,newcountry):
        cls.Country=newcountry
    @classmethod
    def from_str(cls,string):
        params=string.split("-")
        return cls(params[0],params[1],params[2])
    @staticmethod
    def printgood(str):
        print(f"this is a good {str} ")
        return "end"
class Programmer(Employee):
    def __init__(self,aname,asalary,arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language=alanguages
    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    pass
harry=Employee("Harry",3333,"Instructor")
rohan=Employee("Rohan",4444,"student")
shubam=Programmer("Shubham",4433,"cricketer","python")
print(harry.printdetails())
print(shubam.printprog())