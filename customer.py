from database import db_query, mydb

class Customer:
    def __init__(self, username, password, first_name, last_name, date_of_birth, city, account_number):
        self.__username = username
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__city = city
        self.__account_number = account_number

    def createuser(self):
        db_query(
            "INSERT INTO customers (username, password, first_name, last_name, date_of_birth, city, balance, account_number, status) VALUES (%s, %s, %s, %s, %s, %s, 0, %s, 1);",
            (self.__username, self.__password, self.__first_name, self.__last_name, self.__date_of_birth, self.__city, self.__account_number)
        )
        mydb.commit()
