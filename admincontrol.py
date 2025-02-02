import json
import pandas as pd

def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data,f, indent=4)
        
def load_data(filename):
    with open(filename, "r")  as f:
        data=json.load(f)
        return data
        
def enter_data():
    data=load_data('data.json')
    orderid=input("Enter the order id of the product:- ")
    data2={}
    data2["name"]=input("enter the name of the product:- ")
    data2["price"]=int(input("enter the price of the product:- "))
    data2["quantity"]=int(input("enter the quantity of the product:- "))
    data2["category"]=input("enter the category of the product:- ")
    data2["date"]=input("enter the date of the product:- ")
    data[orderid]=data2
    save_data(data,'data.json')
    print("Your data has saved successfully ")
    print("____________________________________________________")

def show_data():
    data=load_data('data.json')
    df=pd.DataFrame.from_dict(data, orient="index")
    print(df)
    print("____________________________________________________")

    
def add():
    enter_data()
    choice=['yes', "y", "no", "n"]
    while True:
        select=input("do you want to continue (yes/no):- ")
        if select in ['yes', "y"]:
            enter_data()
        elif select in ["no", "n"]:
            print("data saved successfully")
            print("____________________________________________________")
            break
            
        else:
            print("invalid input")
            print("____________________________________________________")
    
def update():
    data=load_data('data.json')
    id=input("enter order id you want to update:- ")
    if id in data:
        choice=int(input("enter 1 for update all data or enter 2 for update specific data : - "))
        if choice==1:
            for key in data[id]:
                data[id][key]=input(f"enter  {key} of the product:- ")        
        elif choice==2:
            opt=input("enter attribute name you want to update:- ")
            if opt in data[id]:
                data[id][opt]=input(f"enter value for {opt} :- ")
                save_data(data,'data.json')
                print("data saved successfully ")
                print("____________________________________________________")
            else:
                print("invalid attribute name !")
        else:
            print("invalid chice !")
        save_data(data,'data.json')
        print("data saved successfully ")
    else:
        print("invalid order id !") 
                

def del_specific():
    data=load_data('data.json')
    orderid=input("enter order id you want to delete:- ")
    if orderid in data:
        del data[orderid]
        save_data(data,'data.json')
        print("data delted successfully")
        print("____________________________________________________")
    else:
        print("invalid order id , Please enter valid order id ")

def del_all():
   data={}
   save_data(data, 'data.json')
   print("all data deleted successfully")
   print("____________________________________________________")


