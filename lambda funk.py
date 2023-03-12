#Lambda function or anonymous function
# def min(x,y):
#     return x-y
# print(min(3,4))
#
# minus=lambda x,y:x-y
# print(minus(4,7))

def a_first(a):
    return a[1]
a=[[2,33],[3,6],[1,3] ]
# a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)