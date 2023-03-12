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
class players:
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def playerfunk(self):
        return f"The name is {self.name}. Game is {self.game}"
class coolEmploye(Employee,players):
    language="html"
    def printlanguage(self):
        print(self.language)


karan=coolEmploye("karan",222222,"Coolprog")
harry=Employee("Harry",3333,"Instructor")
rohan=Employee("Rohan",4444,"student")
shubam=players("Shubham","Cricket")
# print(shubam.playerfunk())
print(karan.printdetails())
karan.printlanguage()