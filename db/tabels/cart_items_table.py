from db.db_constants import DBConstants


class CartItemsTable:
    @staticmethod
    def delete_products_from_cart(db_connection):
        cursor = db_connection.cursor()
        delete_orders = f"DELETE FROM lc_cart_items WHERE customer_id={DBConstants.TEST_CUSTOMER_ID}"
        cursor.execute(delete_orders)
        db_connection.commit()
