import admincontrol
import userlogin
import usercontrol
import create_pattern as cp

cp.word("inventory", "#")
print("___________________________________________________________________________________________________________")


def admin_menu():
    print("<-------------ADMIN CONTROL------------>")
    print(" 1. View data")
    print(" 2. Add data ")
    print(" 3. Update data")
    print(" 4. Delete specific data")
    print(" 5. Delete all data")
    print(" 6. Create an Admin")
    print(" 7. Delete an Admin")
    print(" 8. Show Admins")
    print(" 9. Show Adimn info")
    print(" 0. Exit")
    choice=int(input("enter your choice:- "))
    print("__________________________________________________________")
    return choice
    
def admin_functions(choice):
    if choice==1:
        admincontrol.show_data()
        print("_______________________________________________________")
    elif choice==2:
        admincontrol.add()
        print("________________________________________________________")
    elif choice==3:
        admincontrol.update()
        print("________________________________________________________")
    elif choice==4:
        admincontrol.del_specific()
        print("________________________________________________________")
    elif choice==5:
        admincontrol.del_all()
        print("________________________________________________________")
    elif choice ==6:
        userlogin.enter_admin()
        print("________________________________________________________")
    elif choice==7:
        userlogin.del_admin()
        print("________________________________________________________")
    elif choice==8:
        userlogin.show_admin()
        print("________________________________________________________")
    elif choice==9:
        userlogin.show_admin_info()
        print("________________________________________________________")
    

def user_menu():
    print("1. View data")
    print("2. Purchase product")
    print("0. Exit ")
    print("________________________________________________________")
    choice=int(input("enter your choice here:- "))
    return choice
    
def user_control(choice):
    if choice==1:
        admincontrol.show_data()
        print("________________________________________________________")
    elif choice == 2:
        usercontrol.order()
        print("________________________________________________________")
    else:
        print("invalid choice")
        
        
def main():
    while True:
        print(" 1. I am admin")
        print(" 2. I am user ")
        print(" 3. Type -- exit --")
        print("________________________________________________________")
        n=input("enter your choice (1 or 2) :- ")
        if n=="1":
                print("<---------login---------->")
                log=userlogin.login()
                if log == True:
                    choice=admin_menu()
                    if choice==0:
                        print("exited successfully")
                        break
                    admin_functions(choice)
        elif n=="2":
            choice=user_menu()    
            if choice ==0:
                break
            user_control(choice)
        else:
            break 
main()    