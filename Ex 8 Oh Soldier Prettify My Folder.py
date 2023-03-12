import os

path="C:\\Users\\pc\\PycharmProjects\\pythonProject1\\Exercise 8 py"
format=".jpg"
LOF=os.listdir(path)
k=1
def soldier(path,fname,format):
    os.chdir(path)
    os.rename(f"{fname}",f"Image{k}{format}")
for i in range(len(LOF)):
    soldier(path,LOF[i],format)
    k+=1