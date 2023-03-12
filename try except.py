x=input('enter the value of x')
y=input('enter the value of y')
try:
    print(int(x)+y)
except Exception as e:
    print(e)
print('this line is very important')
