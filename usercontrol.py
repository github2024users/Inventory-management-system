import json
import time
import admincontrol

def load_data(filename):
    with open(filename,"r") as f:
        data=json.load(f)
        f.close()
        return data

def save_data(data,filename):
    with open(filename,"w") as f:
        json.dump(data,f)

def order():
    data=load_data("data.json")
    
    name=input("enter your name:- ")
    mob=input("enter your mobile  number:- ")
    id=input("enter the product id :- ")
    
    if id in data:
        prod=data[id]
        quantity=int(input("enter the quantity of the product:- "))
        if quantity <= prod["quantity"]:
            amount=int(prod["price"])*quantity
            tax=amount*0.18
            date_time=time.ctime()
            
            print("_________________________________________________")
            print("name of the product",prod["name"])
            print("category of the product", prod["category"])
            print("The price of this product is :- ",prod["price"])
            print("the quantity of the product is ", quantity)
            print("_________________________________________________")
            print("the amount of the order is :- ", amount)
            print("GST    18% ")
            print("Total mount of the order is :- ", amount+tax)
            print("") 
            print("")
            print(" <----------Thanks for visiting us---------->")
            
            transaction=name+","+mob+","+name+str(quantity)+","+ str(amount)+","+str(date_time)+","+"\n"
            file=open('sales.txt','a')
            file.write(transaction)
            file.close()
        elif quantity > prod["quantity"]:
            print("we have only", prod["quantity"] , "quantity of this product ")
            take=input("do you want to continue with available quantity, press (yes/no):-")
            if take =="yes":
                amount=prod["price"]*prod["quantity"]
                tax=amount*0.18
                total_amount=amount+tax
                print("name of the product",prod["name"])
                print("category of the product", prod["category"])
                print("The price of this product is:- ",prod["price"])
                print("quantity of this product is :- ", prod["quantity"])
                print("_________________________________________________")
                print("the amount of the order is :- ", amount)
                print("GST    18% ")
                print("Total mount of the order is :- ", total_amount)
                print("") 
                print("")
                print(" <----------Thanks for visiting us---------->")
                transaction=name+","+mob+","+name+str(quantity)+","+ str(amount)+","+str(date_time)+","+"\n"
                file=open('sales.txt','a')
                file.write(transactions)
                file.close()
            else:
                print("<----------Thanks for visiting us---------->")
            save_data(data,'data.json')
    else:
            print("wrong order id ")
            inputs=input("do you want to see the products (yes/no):- ")
            if inputs=="yes":
                admincontrol.show_data()
            else:
                print(" <----------Thanks for visiting us ---------->")
            