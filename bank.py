from database import *
import datetime

class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction "
                 f"( timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER )")

    def balance_enquiry(self):
        temp = db_query("SELECT balance FROM customers WHERE username = %s;", (self.__username,))
        print(f"{self.__username} Balance is {temp[0][0]}")

    def deposit(self, amount):
        temp = db_query("SELECT balance FROM customers WHERE username = %s;", (self.__username,))
        test = amount + temp[0][0]
        db_query("UPDATE customers SET balance = %s WHERE username = %s;", (test, self.__username))
        self.balance_enquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f")")
        print(f"{self.__username} Amount is Sucessfully Depositted into Your Account {self.__account_number}")

    def withdraw(self, amount):
        temp = db_query("SELECT balance FROM customers WHERE username = %s;", (self.__username,))
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            test = temp[0][0] - amount
            db_query("UPDATE customers SET balance = %s WHERE username = %s;", (test, self.__username))
            self.balance_enquiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Amount Withdraw',"
                     f"'{amount}'"
                     f")")
            print(f"{self.__username} Amount is Sucessfully Withdraw from Your Account {self.__account_number}")

    def fund_transfer(self, receive, amount):
        temp = db_query("SELECT balance FROM customers WHERE username = %s;", (self.__username,))
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            temp2 = db_query("SELECT balance FROM customers WHERE account_number = %s;", (receive,))
            test1 = temp[0][0] - amount
            test2 = amount + temp2[0][0]
            db_query("UPDATE customers SET balance = %s WHERE username = %s;", (test1, self.__username))
            db_query("UPDATE customers SET balance = %s WHERE account_number = %s;", (test2, receive))
            receiver_username = db_query("SELECT username FROM customers where account_number = %s;", (receive,))
            self.balance_enquiry()
            db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Fund Transfer From {self.__account_number}',"
                     f"'{amount}'"
                     f")")
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Fund Transfer -> {receive}',"
                     f"'{amount}'"
                     f")")
            print(f"{self.__username} Amount is Sucessfully Transaction from Your Account {self.__account_number}")
