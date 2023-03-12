list=['Bhindi','Aloo','Govi','chicken']
# i=1
# for item in list:
#     if i%2!=0:
#         print(item)
#     i+=1
for index,item in enumerate(list):
    if index%2==0:
        print(f"Jarvis please buy {item}")