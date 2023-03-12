print('welcome to printing star programme')
userinp=int(input('Enter any NO.\n'))
boole=int(input('write 0 for false or 1 for true\n'))
k=0
m=userinp
if boole==1:
    while k<userinp+1:
        print(k*'*')
        k+=1
else:
    while m>0:
        print(m*'*')
        m-=1
