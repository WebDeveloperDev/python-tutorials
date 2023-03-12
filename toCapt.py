userinp=input('Enter a Sentence:\n')
x=userinp.split()
k= len(x)
print(k)
print(x)
str=''
for a in range(k):
    str+=x[a].capitalize()+' '
print(str)