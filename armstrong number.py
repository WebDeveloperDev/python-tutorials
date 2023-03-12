from NOD import checkNOD
userinp=int(input('enter your no. to check for armstrong number \n'))
f=userinp
k=checkNOD(userinp)
sum=0
while(userinp>0):
    m=userinp%10
    userinp=int(userinp/10)
    sum+=m**k
if(sum==f):
    print(f," is a armstrong number")
else:
    print(f, " is not a armstrong number")
