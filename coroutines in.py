import time


def searcher():
    book="This is a book which is written by william sexphear"
    time.sleep(3) # This is just to show that a programme is taking some time
    print("before applying")
    while True:
        text=(yield )
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")
# search=searcher()
# next(search)
# search.send("harry")
# input("press any key")
# search.send("This")
# search.close()

#practice
def anotherfunk():
    f1=open("file1.txt","r")
    file1=f1.read()
    f2=open("file2.txt")
    file2=f2.read()
    f3=open("file3.txt")
    file3=f3.read()
    print("i opened all three files")

    while True:
        text=(yield )
        if text in file1 :
            print("your name is there in file1")
        elif text in file2 :
            print("your name is there in file2")
        elif text in file3 :
            print("your name is there in file3")
        else:
            print("your name is not there")
username1=input("Enter your name")
funkvar=anotherfunk()
next(funkvar)
funkvar.send(username1)
print("dowing next time")
username2=input("Enter your name")
funkvar.send(username2)


