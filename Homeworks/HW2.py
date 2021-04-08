
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

def loginSys1(usrname, password):
    if usrname == DEFAULT_USERNAME:    
        if password == DEFAULT_PASSWD:
            return True
        else:
            return False
    else:
        return False


def loginSys2(usrname, password):
    # Flag to check if given username exists
    check = False

    for i in USR_DATABASE.keys():
        if i == usrname:
            check = True

            if USR_DATABASE[i] == password:
                return True
            else:
                return False
            
    if check == False:
        return False


def main():
    # Test 1st login system
    print("--- Login System 1 ---")
    usrname = input("Enter username: ")
    password = input("Enter password: ")
    
    if loginSys1(usrname, password) == True:
        print("Login Successfull!\n")
    else:
        print("Login Failed! Username or password was incorrect\n")

    # Test 2nd login system (With a dictionary)
    print("--- Login System 2 ---")
    usrname = input("Enter username: ")
    password = input("Enter password: ")
    
    if loginSys2(usrname, password) == True:
        print("Login Successfull!")
    else:
        print("Login Failed! Username or password was incorrect")
    

main()
