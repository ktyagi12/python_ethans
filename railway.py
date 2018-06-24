import os

DB_DIR = r'C:\Users\arush\Desktop\upload'
RAIL_DB = {}
VALID_COACHES = ['ac1','ac2','ac3','sl']
VALID_SEAT_PREF = ['L','M','U','N']
PNR = 1

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

def init_db(total_seats=42):
     ac3 = {'L':range(1,total_seats,3),
            'M':range(2,total_seats,3),
            'U':range(3,total_seats,3)}

     ac2 = {'L':range(1,total_seats,2),
            'U':range(2,total_seats,3)}

     ac1 = {'L' : range(1,total_seats)}

     sl = {'L':range(1,total_seats,3),
           'M':range(2,total_seats,3),
           'U':range(3,total_seats,3)}

     RAIL_DB.update({'ac1':ac1,'ac2':ac2,'ac3':ac3,'sl':sl})

def get_vacant_seat(coach,r_nos,seat_pref='U'):
    if len(RAIL_DB[coach][seat_pref]) >= r_nos:
        return RAIL_DB[coach][seat_pref][:r_nos]
    else:
        return False

def reserve_in_db(coach,seat_pref,seats):
    for seat in seats:
        RAIL_DB[coach][seat_pref].remove(seat)

def print_tkt(source,dest,coach,seat_no):
    print '*'*50
    print "PNR    :   0000" + str(PNR)
    print "SOURCE : %s                 DESTINATION : %s" %(source,dest)
    print "COACH : %s" %coach
    print "SEAT NO : %s" %seat_no
    print '*' * 50

def ticket_booking_screen():
    print_header()
    source = raw_input("Enter Source Location : ")
    dest = raw_input("Enter Destination Location : ")
    while True:
        coach = raw_input("Enter the choice of coach(ac1/ac2/ac3/sl): ")
        if coach not in VALID_COACHES:
            print "Please Enter Valid Coach only. \n"
        else:
            break
    no_of_tkt = int(raw_input("Enter number of tickets to book : "))
    while True:
        seat_pref = raw_input("Enter if any seat preference L/M/U/N(no preference) : ")
        if seat_pref not in VALID_SEAT_PREF:
            print "Please ENTER valid seat preference only"
        else:
            break
    if seat_pref != 'N':
        seats = get_vacant_seat(coach,no_of_tkt,seat_pref)
        if not seats :
            print "%s birth not available" %seat_pref
        else:
            reserve_in_db(coach, seat_pref, seats)
            print_tkt(source, dest, coach, seats)

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
            ticket_booking_screen()
        else:
            print '\n'
            print "USer or Password not valid"

    else:
        print '\n'
        print "Please select valid choice"


init_db(42)
while True:
    print '\n' * 2
    main()
