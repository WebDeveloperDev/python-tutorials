# numbers=["3",'6','5','5']
# numbers=list(map(int,numbers))
# print(numbers)
#
# # def sq(a):
# #     return a*a
# list1=[1,3,5,6,4,2,4]
# # list1=list(map(sq,list1))
# list1=list(map(lambda x:x*x,list1))
# print(list1)

list_1=[4,6,2,83,54,5,8,3,4]
def is_greater_5(num):
    return num>5
gr_than5=list(filter(is_greater_5,list_1))
print(gr_than5)