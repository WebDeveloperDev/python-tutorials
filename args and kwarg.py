# def funk1(a,b,c,d):
#     print(a,b,c,d)
# print(funk1('harry','rohan',"shubam",'rohit'))
#args and kwargs are optional
def funk(a,*args,**kwargsbala):
    print(a)
    for item in args:
        print(item)
    for key , value in kwargsbala.items():
        print(f"{key} is a {value}")

har=["Harry","Rohan","Dev","Roshan"]
normal="this is list of students"
kw={"Harry":"web developer","Dev":"junior web developer","Rohan":"inspector","Jeet":"home designer"}
funk(normal,*har,**kw)