# f= open('harry.txt', "w") #write
# f= open('harry.txt', "a") #append
# f.write('harry bhai bhot acche hai\n')
# f.close()

# Handle read and write both
f=open('harry.txt','r+')
print(f.read())
f.write("Thank you \n llllll")