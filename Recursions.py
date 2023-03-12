def print2(str1):
    # print2(str1)
    print("this is  " +str1)
print2("Harry")
def factorial_itrative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
print(factorial_itrative(3)) #itration method

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_itrative(n-1)
print(factorial_recursive(3)) #recursive method

#quiz
# x=0
# y=1
# z=1
# k=0
# while(k<10):
#     x=y
#     y=z
#     z=x+y
#     print(z)
#     k+=1

# 0 1 1 2 3 5 8
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))