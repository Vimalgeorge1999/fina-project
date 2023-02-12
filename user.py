import json
import sys
class user:
    def __init__(self):
        self.signin_det={}
    def user_sign(self):
        self.name=input("enter your name:")
        self.phonenumber=int(input("enter your phine number:"))
        self.email=input("enter your email:")
        self.address=input("enter your address:")
        self.password=int(input("enter ypur passwoerd:"))
        self.signin_det={"name":self.name,"phonenumber":self.phonenumber,"email":self.email,"address":self.address,"password":self.password}
        with open( "userdetails.json","w") as f:
            json.dump(self.signin_det,f)
        return self.signin_det
    def login(self,email,password):
        with open("userdetails.json","r") as f:
            m=json.load(f)
        if email!=m["email"]:
            print("enter registerd mail id")
            sys.exit()
        else:
            if password!=m["password"]:
                print("enter a valid password")
            else:
                print("log in successfull")
                return ""
    def update_profile(self):
        self.signin_det["name"]=input("enter the updated name:")
        self.signin_det["phonenumber"]=int(input("enter the updated phonenumber:"))
        self.signin_det["email"]=input("enter the updated emailid:")
        self.signin_det["address"]=input("enter the updated address:")
        self.signin_det["password"]=input("enter the updated pasword:")
    def new_order(self):
        while True:
            print("*"*50)
            print("press 1 for tandoori chicken" )
            print("press 2 for vegan burger" )
            print("press 3 for truffle cake" )
            print("*" *50)
            option=int(input("choose your number for the order"))
            print("*"*50)
            if option==1:
                print("successfylly ordered thandoori chicken, RS: 240 INR")
            elif option==2:
                print("successfylly ordered vegan burger, RS: 320 INR")
            elif option==3:
                print("successfylly ordered truffle cake, RS: 900 INR")
            else:
                print("plse enter a valid input")

print("welcome to VIMALS RESTAURANT")
print("*"*50)
x=user()
while True:
    print("*"*50)
    print("press 1 for REGISTRATION" )
    print("press 2 for LOG IN" )
    print("press 3 for UPDATE PROFILE" )
    print("press 4 for NEW ORDER")
    print("*" *50)
    option=int(input("choose your OPTION for the processing"))
    print("*"*50)
    if option==1:
        x.user_sign()
    elif option==2:
        email=input("enter the mail id:")
        password=int(input("enter the password:"))
        x.login(email,password)
    elif option==3:
        x.update_profile()
    elif option==4:
        x.new_order()
    else:
        print("plse enter a valid input")








    