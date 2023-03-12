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
    pass
harry=Employee("Harry",3333,"Instructor")
rohan=Employee("Rohan",4444,"student")
karan=Employee.from_str("Karan-454-student")
harry.change_country("indonesia")
print(karan.salary)
print(karan.printgood(str))