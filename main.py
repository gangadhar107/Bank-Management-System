from register import SignUp, SignIn
from bank import Bank
from database import db_query, mydb

def main_menu():
    while True:
        print("Welcome to the Bank of KKD Banking System")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            SignUp()
        elif choice == '2':
            result = SignIn()
            if result:
                username, first_name = result
                user_menu(username, first_name)
        elif choice == '3':
            print("Thanks for using our banking services. If you need them again, feel free to return. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(username, first_name):
    account_number = db_query("SELECT account_number FROM customers WHERE username = %s;", (username,))[0][0]
    bobj = Bank(username, account_number)
    while True:
        print(f"\nWelcome, {first_name}")
        print("1. Balance Enquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Fund Transfer")
        print("5. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            bobj.balance_enquiry()
        elif choice == '2':
            handle_deposit(bobj)
        elif choice == '3':
            handle_withdraw(bobj)
        elif choice == '4':
            handle_fund_transfer(bobj)
        elif choice == '5':
            print("Thanks for using our banking services. If you need them again, feel free to return. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_deposit(bobj):
    while True:
        try:
            amount = int(input("Enter Amount to Deposit: "))
            bobj.deposit(amount)
            mydb.commit()
            break
        except ValueError:
            print("Enter Valid Input (Numbers Only)")

def handle_withdraw(bobj):
    while True:
        try:
            amount = int(input("Enter Amount to Withdraw: "))
            bobj.withdraw(amount)
            mydb.commit()
            break
        except ValueError:
            print("Enter Valid Input (Numbers Only)")

def handle_fund_transfer(bobj):
    while True:
        try:
            receive = int(input("Enter Receiver Account Number: "))
            amount = int(input("Enter Money to Transfer: "))
            bobj.fund_transfer(receive, amount)
            mydb.commit()
            break
        except ValueError:
            print("Enter Valid Input (Numbers Only)")

if __name__ == "__main__":
    main_menu()
