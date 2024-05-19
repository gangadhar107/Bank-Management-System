from customer import Customer
from bank import Bank
from database import db_query
import random

def SignUp():
    while True:
        username = input('Create Your Username: ')
        temp = db_query("SELECT username FROM customers WHERE username = %s;", (username,))
        if temp:
            print("Entered Username is already taken. Please try a different one.")
        else:
            break

    print("Username is available. Please proceed.")
    password = input("Enter Your Password: ")
    first_name = input("Enter Your First Name: ")
    last_name = input("Enter Your Last Name: ")
    date_of_birth = input("Enter Your Date of Birth (YYYY-MM-DD): ")
    city = input("Enter Your City: ")

    while True:
        account_number = random.randint(10000000, 99999999)
        temp = db_query("SELECT account_number FROM customers WHERE account_number = %s;", (account_number,))
        if temp:
            continue
        else:
            print("Your Account Number: ", account_number)
            break

    cobj = Customer(username, password, first_name, last_name, date_of_birth, city, account_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()


def SignIn():
    while True:
        username = input("Enter Username: ")
        temp = db_query("SELECT username, first_name FROM customers WHERE username = %s;", (username,))
        if temp:
            while True:
                password = input(f"Welcome {temp[0][1]}. Enter Password: ")
                temp_password = db_query("SELECT password FROM customers WHERE username = %s;", (username,))
                if temp_password[0][0] == password:
                    print("Your Sign In Was Successful")
                    return username, temp[0][1]
                else:
                    print("Wrong Password. Try Again.")
        else:
            print("Enter Correct Username")
