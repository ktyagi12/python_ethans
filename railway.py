import os

DB_DIR = r'C:\Users\arush\Desktop\upload'


def print_header():
    print '-'*50
    print "       WELCOME TO INDIAN RAILWAYS"
    print '-'*50

def first_screen():
    print "\n"
    print "Enter your choice:-"
    print r'(1) Register'
    print r'(2) Login'
    valid_choices = [1,2]
    choice = int(raw_input("choice : "))
    if choice not in valid_choices:
        print '\n'
        print "Please Enter a valid choice only"
        first_screen()
    else:
        return choice

def input_password(check=True):
    password = raw_input("Enter Password :")
    if check and len(password) == 0 :
        print '\n'
        print "Enter password with atleast one char"
        input_password()
    return password

def input_user_name():
    user_name = raw_input("Enter user name :")
    if not user_name:
        print '\n'
        print "Enter valid user name"
        input_user_name()
    return user_name

def register_user():
    user_name = input_user_name()
    password = input_password()
    if check_user_exist(user_name):
        print '\n'
        print "User Already Exists"
        return 1
    else:
        create_user_passwd_file(user_name,password)
        print '\n'
        print "User Registration Successful"

def check_user_exist(user_name):
    user_file = user_name + r'.txt'
    if os.path.exists(os.path.join(DB_DIR,user_file)):
        return True
    else:
        False

def create_user_passwd_file(user_name,password):
    user_file = user_name + r'.txt'
    fd = open(os.path.join(DB_DIR,user_file),'w')
    fd.write(password)
    fd.close()

def verify_password(user_name,password):
    if check_user_exist(user_name):
        user_file = user_name + r'.txt'
        fd = open(os.path.join(DB_DIR,user_file))
        act_paswd = fd.read()
        if act_paswd == password:
            return True
        else:
            return False
    else:
        return False

def main():
    print_header()
    choice = first_screen()
    if choice == 1:
        register_user()
    elif choice == 2:
        user_name = input_user_name()
        password = input_password(check=False)
        if verify_password(user_name,password):
            print '\n'
            print "Login Successful"
        else:
            print '\n'
            print "USer or Password not valid"

    else:
        print '\n'
        print "Please select valid choice"


while True:
    print '\n' * 2
    main()