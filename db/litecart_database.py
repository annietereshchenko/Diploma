import mysql.connector
from mysql.connector import Error


def get_db_connection(host_name, user_name, user_password, db_name):
    my_connection = None
    try:
        my_connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print('succes')
    except Error as e:
        print(f'The error {e} occurred')
    return my_connection


connection = get_db_connection('127.0.0.1', 'root', '', 'litecart')
cursor = connection.cursor()
get_orders = f'SELECT * FROM lc_orders WHERE customer_id=2'
cursor.execute(get_orders)
list_of_orders = cursor.fetchall()
print(len(list_of_orders))

connection.close()
