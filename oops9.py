class Dad:
    basketball=6
class Son(Dad):
    dance=1
    def isdance(self):
        return f"I dance {self.dance} no. of times"
class Grandson(Son):
    dance = 9
    def isdance(self):
        return f"I dance awesomely {self.dance} number of times"

darry=Dad()
larry=Son()
harry=Grandson()
# print(harry.isdance())
# print(harry.dance)
#quiz
class ElectronicDevice:
    no_of_devices=4
    def __init__(self,a,b,c,d):
        self.Elec_list=[a,b,c,d]
class pocket_gadget(ElectronicDevice):
    # no_of_devices=2
    def __init__(self,a,b):
        self.pocket_list=[a,b]
class phone(pocket_gadget):
    # no_of_devices=1
    def __init__(self,a):
        self.phone_list=[a]
machine=ElectronicDevice("car","bike","computer","mixer")
computer=pocket_gadget("phone","perfume")
mobile=phone("mobile")
print(mobile.no_of_devices)
