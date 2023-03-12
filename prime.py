userinp=int(input('Enter the limit\n'))
for num in range(userinp+1):
    i=2
    while(i<num):
        if(num%i==0):
            break
        i+=1
    else:
        print(num, " is prime number")
