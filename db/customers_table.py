from .db_constants import DBConstants


def get_test_user_names_by_id(db_connection):
    cursor = db_connection.cursor()
    get_user_by_id_query = f'SELECT firstname, lastname FROM lc_customers WHERE id={DBConstants.TEST_CUSTOMER_ID}'
    cursor.execute(get_user_by_id_query)
    list_of_names = cursor.fetchall()
    return list_of_names[0]
