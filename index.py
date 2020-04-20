import dia_profile
import register_patient
class Index:
    def user_login(self):
        print("********Welcome*******")
        print("----Diabetes Monitoring-----")
        ch = input("Do you want to Login = L/Register = R: ")
        if ch.upper() == "L":
            dia_profile.Diabetes_profile().profile_report()
        elif ch.upper() == "R":
            register_patient.Register().user_register()

def main():
    Index().user_login()
main()