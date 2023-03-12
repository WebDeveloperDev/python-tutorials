f= open('harry.txt')
# print(f.tell()) #it tell the position of file pointer
print(f.readline())
# print(f.tell())
f.seek(0) #it seek the file pointer
print(f.readline())
f.close()