f=open('harry.txt',"r")
# content =f.read()
# content =f.read(5) # it will read 5 char.
# print(content)
# content=f.read(4)
# print(content)
# print(f.readline())
# print(f.readline())
for line in f:
    print(line)
f.close()
