def menu():
    loop='y'
    while(loop=='y' or loop=='Y'):
        print("menu")
        print("1.Insert")
        print("2.Update")
        print("3.Delete")
        print("4.Display")
        print("5.Search")
        print("6.Exit")
        choice=int(input("Enter the choice "))
        if choice==1:
            insert()
        elif choice==2:
            update()
        elif choice==3:
            delete()
        elif choice==4:
            display()
        elif choice==5:
            search()
        else:
            break
        loop=input("type 'y' if u want to continue")
    else:
        sys.exit()

def insert():
    import mysql.connector as sql
    con=sql.connect(host='localhost',user='root',password='Ddms@Porps@123')
    cur=con.cursor()
    Train_No=int(input("enter train.no: "))
    Train_Name=input("enter train name: ")
    Time_arrival=str(input("enter time of arrival: "))
    Time_Dept=str(input("enter time of departure: "))
    rec="insert into train(Train_No,Train_Name,Time_arrival,Time_Dept) values({},'{}','{}','{}')".format(Train_No,Train_Name,Time_arrival,Time_Dept)
    cur.execute("use railyatri;")
    cur.execute(rec)
    con.commit()
    print("successful")
    con.close()

def update():
    import mysql.connector as sql
    con=sql.connect(host='localhost',user='root',password='Ddms@Porps@123')
    cur=con.cursor()
    d=int(input("enter train no for update: "))
    Train_No=int(input("enter new train.no: "))
    Train_Name=input("enter new train name: ")
    Time_arrival=str(input("enter new time of arrival: "))
    Time_Dept=str(input("enter new time of departure: "))
    rec="update train set Train_No=%s, Train_Name='%s', Time_arrival='%s', Time_Dept='%s' where Train_No=%s" % (Train_No,Train_Name,Time_arrival,Time_Dept,d)
    cur.execute("use railyatri;")
    cur.execute(rec)
    con.commit()
    print("Updated")
    con.close()

def delete():
    import mysql.connector as sql
    con=sql.connect(host='localhost',user='root',password='Ddms@Porps@123')
    cur=con.cursor()
    d=int(input("enter train no for deleting record: "))
    rec="delete from train where Train_No={0}".format(d)
    cur.execute("use railyatri;")
    cur.execute(rec)
    con.commit()
    print("deleted")
    con.close()

def display():
    import mysql.connector as sql
    con=sql.connect(host='localhost',user='root',password='Ddms@Porps@123')
    cur=con.cursor()
    cur.execute("use railyatri;")
    cur.execute('select * from train')
    rec=cur.fetchall()
    count=cur.rowcount
    print(rec)

def search():
    import mysql.connector as sql
    con=sql.connect(host='localhost',user='root',password='Ddms@Porps@123')
    cur=con.cursor()
    print("1.according to train.no")
    print("2.according to train name")
    choice=int(input("enter ur choice"))
    if choice==1:
        d=int(input("enter train no to be searched: "))
        rec="select * from train where Train_No=%s" %(d)
    elif choice==2:
        name=input("enter train name to be searched: ")
        rec="select * from train where Train_Name='%s'" %(name)
    else:
        print("wrong choice")
    cur.execute("use railyatri;")
    cur.execute(rec)
    ch=cur.fetchall()
    count=cur.rowcount
    print("No. of records found=",count)
    for i in ch:
        print(i)
    print("searched")
    con.close()

import mysql.connector as sql
con=sql.connect(host='localhost',user='root',password='Ddms@Porps@123')
cur=con.cursor()
cur.execute("create database railyatri;")
cur.execute("use railyatri;")
cur.execute("create table train ( Train_No int(5) not null primary key,Train_Name varchar(30) not null,Time_arrival time not null,Time_Dept time not null);")
cur.execute("insert into train values (10001,'Ajanta','07:00','07:15'),(10002,'Ananya','07:30','07:45'),(10003,'Chambal','08:00','8:05');")
con.commit()
con.close()
menu()        
