import pickle

#Pickling a python obj
# cars=["Audi","BMW","Maruti Suzuki","Harryti Tuzuki"]
# file="mycar.pkl"
# fileobj=open(file,"wb")
# pickle.dump(cars,fileobj)
# fileobj.close()

file="mycar.pkl"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)