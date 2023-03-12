class Employee:
    country="India"
    pass
harry=Employee()
rohan=Employee()
harry.name="Harry singh"
rohan.name="Rohan paal"
harry.salary=3333
rohan.salary=4333
harry.role="Instructor"
rohan.role="Student"
rohan.country="Nepal"
print(harry.role,harry.country,rohan.country)
Employee.country="France"
print(Employee.country)
print(rohan.__dict__)