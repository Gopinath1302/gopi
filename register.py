import re
name=["balaji","Dinesh","Gowtham","Sridhar","Seeniduari"]
number=[6381061323,7339597374,9360782181,8438773480,7639971597]
user_name=["Bala@123","Dinesh@123","Gowtham2123","Sri@123","Seeni@123"]
password=["Bala@123","Dinesh@123","Gowtham2123","Sri@123","Seeni@123"]
class Register:
    @classmethod
    def details(self):
        print("Enter your name")
        name1=input()
        name.append(name1)
        flag=1
        while flag:
          mobile_number1=int(input("Enter your Mobile Number" ))
          if mobile_number1 > 6000000000 and mobile_number1 < 9999999999:
           number.append(mobile_number1)
           flag-=1
          else:
              print("Valid Mobile Number")
        flag=True
        while flag:
          print("Enter your User_name")
          user_name1=input()
          regex = ("(?=.*[a-z])(?=.*[A-Z]).+$")
          constraint = re.compile(regex)
          if (re.search(constraint,user_name1)):
              flag=False
              user_name.append(user_name1)
          else:
            print("Enter User name again")
        flag=True
        while flag:
         print("Enter Password")
         password1=input()
         regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$"
         constraint = re.compile(regex)
         if(re.search(constraint,password1)):
           flag=False
           password.append(password1)
         else:
             print("Try another password")
        print("Confirm password")
        c_password=input()
        if password1 == c_password :
            print("Registered Succesfully")
            new1.check()
class login():            
    def check(self):
        print("_________ Log-In____________")
        print("Enter Your Username")
        useR_nAme=input()
        print("Enter Your Password")
        paSS=input()
        for i in range(len(name)):
         if useR_nAme == user_name[i]:
          if paSS== password[i]:
            print("welcome to book store")
new1= login()