import time
initial =time.time()
print(initial)
k=0
while k<45:
    print("this is harry bhai")
    time.sleep(2) #it sleeps the time for 2 second
    k+=1
print("while loop ran in",time.time()-initial, "seconds")
# initial2=time.time()
# for i in range(45):
#     print("This is Harry bhai")
# print("for loop ran in " ,time.time()-initial2,"seconds")

# localtime=time.asctime((time.localtime(time.time())))
# print(localtime)