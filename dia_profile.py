from pylab import *
import sqlite3
import register_patient
con=sqlite3.connect("diabetes.db")

class Diabetes_profile:
    def profile_report(self):
        cur = con.cursor()
        phone = input("Enter the phone number: ")
        cur.execute("SELECT * FROM user WHERE number = :1", {'1': phone})
        data = cur.fetchall()

        if len(data) > 0:
            print(data)
            print("Login Successful *_*")
            cur.execute("SELECT * FROM report WHERE number = :1",{'1': phone})
            print(cur.fetchall())
            ch = input("Do you want to enter the report(Y/N): ")
            if ch.upper() == "Y":
                date = input("Enter the date: ")
                type_test = input("Type of testing(RBS / FBS/PPBS): ")
                if type_test.upper() == "RBS":
                    report = int(input("Enter the report: "))
                    if report < 190:
                        final_report = "Normal"
                    elif report >= 190:
                        final_report = "Diabetes"
                elif type_test.upper() == "FBS":
                    report = int(input("Enter the report: "))
                    if report < 110:
                        final_report = "Normal"
                    elif report >= 110:
                        final_report = "Diabetes"
                elif type_test.upper() == "PPBS":
                    report = int(input("Enter the report: "))
                    if report < 160:
                        final_report = "Normal"
                    elif report >= 160:
                        final_report = "Diabetes"
                print(report," "+final_report)
                cur.execute("INSERT INTO report VALUES(:1,:2,:3,:4,:5)",(date,phone,report,final_report,type_test))
                con.commit()
                cur.execute("SELECT Report FROM report WHERE number = :1", {'1': phone})
                data = cur.fetchall()
                li = []
                for i in data:
                    li.append(i[0])
                plot(arange(1, len(li)+1), li)
                xlabel('mg/dl')
                ylabel('No of Visits')
                title('Diabetes Monitor')
                legend(('sample1', 'sample2'))
                savefig("sampleg.png", dpi=(640 / 8))
        else:
                print("New User .. Please Register")
                register_patient.Register().user_register()
        con.close()