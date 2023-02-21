from register import Register
from register import login
class Choise():
    def __init__(self):
        print("Enter 1 for Register")
        print("Enter 2 for Login")
        print("Enter 3 for Logout")
        op=int(input())
        if op==1:
            Register.details()
        elif op==2:
            new=login()
            new.check()
        elif op==3:
            print("logout")
        else:
            print("Enter option Correctly")