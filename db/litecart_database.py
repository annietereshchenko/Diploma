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
    except Error as e:
        print(f'The error {e} occurred')
    return my_connection
