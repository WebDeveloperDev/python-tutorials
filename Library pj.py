# Create a libraty class
# display book
# lend book
# return book
# HarryLibrary =Library(listofbooks,library name )
import ast
print("Welcome to Library")
booked=[]
with open("lib data.txt","r") as f:
    # print(f.readline())
    for i in f:
     data=ast.literal_eval(i)
     booked.append(data)

print(booked)
Lob=["Ben Hur","Around the World in eighty days","Baburnama", "Anna Karenina","Arthashastra","Pride and Prejudice","In Search of Lost Time by Marcel Proust."," Ulysses by James Joyce",". Don Quixote by Miguel de Cervantes.","One Hundred Years of Solitude by Gabriel Garcia Marquez"," The Great Gatsby by F","Moby Dick by Herman Melville","War and Peace by Leo Tolstoy","Hamlet by William Shakespeare"]
class Library:
    def __init__(self,name):
        self.name=name
    @classmethod
    def DpB(cls):
        for item in Lob:
            print(f"{Lob.index(item)}. {item}")
    @classmethod
    def LendBook(cls,name,book):
        j=True
        for i in booked:
            varp=list(i.keys())[0]
            varv=list(i.values())[0]
            # print(list(varp)[0])
            if Lob[book]==varv:
                # print(list(booked.keys())[list(booked.values()).index(var)])
                # cam=list(i.keys())[list(i.values()).index(book)]
                print(f"The book is sold to {varp}")
                j=False
            # print(j)
        if j==True:
            k={name:Lob[book]}
            booked.append(k)
            print(f"{Lob[book]} book has been purchased")
    @classmethod
    def listofbookbyname(cls,name):
        lop=[]
        for i in booked:
            varp=list(i.keys())[0]
            varv=list(i.values())[0]
            if name==varp:
                lop.append(varv)
        print(f"{name} your list of book: \n{lop}")
    @classmethod
    def ReturnBook(cls,name):
        lop = []
        for i in booked:
            varp = list(i.keys())[0]
            varv = list(i.values())[0]
            if name == varp:
                lop.append(varv)
        print(lop,"lop var")
        print(f"{name} your list of book :")
        for i in lop:
            print(f"{lop.index(i)}. {i}")
        userret=int(input("Enter the index no. of book which you want to return"))
        if len(lop)>userret:
            for i in booked:
                if lop[userret]==list(i.values())[0]:
                    print(i)
                    booked.remove(i)
            lop.remove(lop[userret])
            print("The book is successfully returned")
        else:
            print("No book exist in this index number")

                # del i
while True:
    username=input("Enter your name or press 0 to exit\n")
    if username=="0":
        break
    ClsObj=Library(username)
    C=True
    while C==True:
        userinput=int(input("press 1 to buy the book\npress 2 to see the list of your books\npress 3 to return the book\npress other number to back to menu "))
        inside=True
        if userinput==1:
            while inside==True:
                ClsObj.DpB()
                booking=int(input("Enter the index no. of the book which you have to Lend"))
                if booking>len(Lob):
                    print("no book exit")
                else:
                    ClsObj.LendBook(username,booking)
                # print(Lob)
                # print(booked)
                cont= input("Enter 'c' to continue\nEnter b to back one step or 'm' for menu").capitalize()
                if cont=="C":
                    continue
                elif cont=="B":
                    inside=False
                else:
                    C=False
                    inside=False
        elif(userinput==2):
            ClsObj.listofbookbyname(username)
        elif(userinput==3):
            ClsObj.ReturnBook(username)
        else:
            C==False
with open("lib data.txt","w") as f:
    # f.seek(0)
    # f.write("")
    # f.write()
    # f.write("s")
    for i in booked:
        f.write(f"{i}\n")