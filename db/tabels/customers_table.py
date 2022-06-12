from db.db_constants import DBConstants
from helpers.testing_data import TestUserData


class CustomerTables:
    @staticmethod
    def get_test_user_names_by_id(db_connection):
        cursor = db_connection.cursor()
        get_user_by_id_query = f'SELECT firstname, lastname FROM lc_customers WHERE id={DBConstants.TEST_CUSTOMER_ID}'
        cursor.execute(get_user_by_id_query)
        list_of_names = cursor.fetchall()
        return list_of_names[0]

    @staticmethod
    def revert_user_names(db_connection):
        cursor = db_connection.cursor()
        update_user_names = f"UPDATE lc_customers SET firstname = '{TestUserData.FIRST_NAME}', " \
                            f"lastname = '{TestUserData.LAST_NAME}' WHERE id={DBConstants.TEST_CUSTOMER_ID}"
        cursor.execute(update_user_names)
        db_connection.commit()
