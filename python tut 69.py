class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "email is not set please set your email using setter"
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,str):
        names=str.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
person1=Employee("Dev","Solanki")
# person2=Employee("Raj","sahu")
print(person1.email)
person1.fname="Satyam"
person1.email="This.that@gmail.com"
del person1.email
print(person1.fname)
person1.email="Harry.Perry@gmail.com"
print(person1.email)
skillf=Employee("Skill","f")
print(skillf.email)
#Inspect
print(type(skillf))
print(id(skillf))
print(dir(skillf))
import inspect
print(inspect.getmembers(skillf))