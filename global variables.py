l=10 # Global variable
def funk(n):
    # l=5 #Local variable
    global l
    l=l+4
    print(l)
    print(n," I have printed")
funk(3)
print(l)