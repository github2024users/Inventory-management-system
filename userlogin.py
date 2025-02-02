import json
import pandas as pd

def save_admin(data,filename):
    with open(filename,"w") as f:
        json.dump(data, f, indent=4)
        
def load_admin(filename):
    with open(filename,"r") as f:
        data=json.load(f)
        return data

def enter_admin():
    data=load_admin('userlogin.json')
    name=input("enter your name:- ")
    data2={}
    while True:
        data2["uid"]=input("create username:- ")
        if any(user["uid"]==data2["uid"] for user in data.values()):
            print("username already exist  ")
        else:
            break
    data2["pwd"]=input("create  your password")
    data[name]=data2
    save_admin(data,'userlogin.json')

def show_admin_info():
    data=load_admin('userlogin.json')
    df=pd.DataFrame.from_dict(data, orient="index")
    print(df)
    
def show_admin():
    data=load_admin('userlogin.json')
    for key in data:
        print(key)

def login():
    data = load_admin('userlogin.json')
    usid = input("Enter your user ID: ")
    pswd = input("Enter your password: ")
    for key in data:
        if data[key]["uid"] == usid and data[key]["pwd"] == pswd:
            print('LOGIN SUCCESSFUL')
            return True
    print("Invalid login ID or password!")
    return False
    
def del_admin():
    data=load_admin('userlogin.json')
    name=input("enter the name of admin to be delete")
    del data[name]
    save_admin(data,'userlogin.json')
    print("admin deleted successfully")


