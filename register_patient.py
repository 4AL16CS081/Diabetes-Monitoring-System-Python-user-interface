import sqlite3
con=sqlite3.connect("diabetes.db")

class Register:
    def user_register(self):
        cur = con.cursor()
        name=input("enter the patient Name: ")
        age=int(input("enter the Age: "))
        sex=input(" enter the Sex: ")
        phone=int(input("enter the Number: "))
        address=input("enter the Address: ")
        cur.execute("INSERT INTO user VALUES(:1,:2,:3,:4,:5)",(phone,name,age,sex,address))
        con.commit()
        con.close()