class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="I am inside class A's constructor"
        self.special="This var should be print"
        # self.classvar1="Instance var in class A"
class B(A):
    classvar2="I am in class B"
    def __init__(self):
        super().__init__()
        self.var1="I am inside class B's constructor"
        self.classvar2="Instance var in class B"
a=A()
b=B()
print(b.classvar1)
print(b.special)