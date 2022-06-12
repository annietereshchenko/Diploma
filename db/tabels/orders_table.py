from db.db_constants import DBConstants


class OrdersTable:
    @staticmethod
    def get_orders_by_customer_id(db_connection):
        cursor = db_connection.cursor()
        get_orders = f'SELECT * FROM lc_orders WHERE customer_id={DBConstants.TEST_CUSTOMER_ID}'
        cursor.execute(get_orders)
        list_of_orders = cursor.fetchall()
        return len(list_of_orders)

    @staticmethod
    def delete_orders_of_customer(db_connection):
        cursor = db_connection.cursor()
        delete_orders = f"DELETE FROM lc_orders WHERE customer_id={DBConstants.TEST_CUSTOMER_ID}"
        cursor.execute(delete_orders)
        db_connection.commit()
