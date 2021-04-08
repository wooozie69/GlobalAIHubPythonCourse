
# Sample global variables for 1st login system
DEFAULT_USERNAME = "test"
DEFAULT_PASSWD = "1234"

# Sample global dictionary for 2nd login system
USR_DATABASE = {
        "Okarin" : "2010ElPsyCongroo",
        "GlobalAIHub" : "1ntroToPyth0n",
        "root" : "alpine",
        "test" : "1234"
    }

def loginSys1():
    print("--- Login System 1 ---")
    
    # Read username from user
    usrname = input("\nEnter username: ")
    if usrname == DEFAULT_USERNAME:
        
        # Now read password from user
        password = input("Enter password: ")
        
        if password == DEFAULT_PASSWD:
            print("Login Successfull!")
        else:
            print("Login Failed! Passwords doesn't match for this user!")

    else:
        print("Login Failed! This user doesn't exist!")


def loginSys2():
    print("--- Login System 2 ---")
    
    # Flag to check if given username exists
    check = False
    
    # Read username from user
    usrname = input("\nEnter username: ")
    for i in USR_DATABASE.keys():
        
        if i == usrname:
            check = True
            
            # Read password from user
            password = input("Enter password: ")
            
            if USR_DATABASE[i] == password:
                print("Login Successfull!")
            else:
                print("Login Failed! Passwords doesn't match for this user!")

    if check == False:
        print("Login Failed! This user doesn't exist!")


loginSys1()
print()
loginSys2()
