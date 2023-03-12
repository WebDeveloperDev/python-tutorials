# class Employee:
#     Country="INDIA"
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#     def printdetails(self):
#         return f"Name is {self.name} . Salary is {self.salary} and role is {self.role}"
#     @classmethod
#     def change_country(cls,newcountry):
#         cls.Country=newcountry
#     @classmethod
#     def from_str(cls,string):
#         params=string.split("-")
#         return cls(params[0],params[1],params[2])
#
# # Create a libraty class
# # display book
# # lend book
# # return book
# # HarryLibrary =Library(listofbooks,library name )
# print("Welcome to Library")
# booked=[]
# Lob=["Ben Hur","Around the World in eighty days","Baburnama", "Anna Karenina","Arthashastra","Pride and Prejudice","In Search of Lost Time by Marcel Proust."," Ulysses by James Joyce",". Don Quixote by Miguel de Cervantes.","One Hundred Years of Solitude by Gabriel Garcia Marquez"," The Great Gatsby by F","Moby Dick by Herman Melville","War and Peace by Leo Tolstoy","Hamlet by William Shakespeare"]
# class Library:
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def DpB(cls):
#         for item in Lob:
#             print(f"{Lob.index(item)}. {item}")
#     @classmethod
#     def LendBook(cls,name,book):
#         k={name:Lob[book]}
#         booked.append(k)
#         print(f"{Lob[book]} book has been purchased")
#         # Lob.remove(book)
# username=input("Enter your name\n")
# ClsObj=Library(username)
# k=True
# while k==True:
#     ClsObj.DpB()
#     booking=int(input("Enter the index no. of the book which you have to Lend"))
#     ClsObj.LendBook(username,booking)
#     print(Lob)
#     print(booked)
#     cont= input("Enter 'c' to continue or 'e' to exit").capitalize()
#     if cont=="C":
#         continue
#     else:
#         k=False
#     pass
# harry=Employee("Harry",3333,"Instructor")
# rohan=Employee("Rohan",4444,"student")
# karan=Employee.from_str("Karan-454-student")
# harry.change_country("indonesia")
# print(karan.salary)
# # print(harry.role)
# # print(harry.Country)
# # print(rohan.role)
#
#
#
# # rohan=Employee()
# # harry.name="Harry singh"
# # rohan.name="Rohan paal"
# # harry.salary=3333
# # rohan.salary=4333
# # harry.role="Instructor"
# # rohan.role="Student"
# # rohan.country="Nepal"
# # print(rohan.printdetails())
