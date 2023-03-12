import mysql.connector as mycon
cn=mycon.connect(host='localhost',user='root',password='mysql@123',database="devendra")
cr=cn.cursor()
print(cn)
# username=input('Enter your name')
# address=input('Enter your address')
# cr.execute('''insert into firsttable values(%s, %s);''',[username,address])
# cn.commit()
cr.execute("SELECT * from firsttable")
myresult=cr.fetchall()
print(myresult)
for raw in myresult:
    print(raw)