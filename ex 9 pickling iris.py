import pickle

with open("iris.data","r") as f:
    data=f.read().splitlines()
    print(data)

#pickling file
with open("iris.pkl","wb") as fileobj:
    pickle.dump(data,fileobj)
#reading pickle as a list
with open("iris.pkl","rb") as fileobj1:
    read=pickle.load(fileobj1)
    print(read)