# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
ls=[i for i in range(100) if i%3==0]
print(ls)
dict1={i:f"item{i}" for i in range(100)}
dict1={value:key for key,value in dict1.items()}
print(dict1)

dresses={dress for dress in ["dress1","dress2","dress1","dress1"]} #Set comprehensions
print(dresses)