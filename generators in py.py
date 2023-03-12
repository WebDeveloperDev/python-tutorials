"""
itrable
itrator
itration
"""
def gen(n):
    for i in range(n):
        yield i
g=gen(12)
# print(g)
# print(g.__next__())
# print(g.__next__())
# for i in g:
#     print(i)
h="harry" #String is iterable
ier=iter(h)
print(ier.__next__())
# for c in h:
#     print(c)

#quick quiz
def funk():
    x=0
    y=0
    z=1
    while True:
        x=y
        y=z
        z=x+y
        yield z
k=funk()
print(k)
print(k.__next__())
print(k.__next__())
print(k.__next__())
print(k.__next__())
