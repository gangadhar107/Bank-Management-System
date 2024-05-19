import mysql.connector as sql
import os

# Fetching database credentials from environment variables
host = os.getenv("DB_HOST", "localhost")
user = os.getenv("DB_USER", "root")
passwd = os.getenv("DB_PASS", "password")# Substitute password with your database password. 
database = os.getenv("DB_NAME", "database")# Substitute database with your database name.

mydb = sql.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database
)

cursor = mydb.cursor()

def db_query(query, params=None):
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sql.Error as e:
        print(f"Error: {e}")
        return None

def create_customer_table():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                first_name VARCHAR(20) NOT NULL,
                last_name VARCHAR(20) NOT NULL,
                date_of_birth DATE NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                status BOOLEAN NOT NULL
            )
        ''')
        mydb.commit()
    except sql.Error as e:
        print(f"Error: {e}")
        mydb.rollback()


if __name__ == "__main__":
    create_customer_table()
    cursor.close()
    mydb.close()
