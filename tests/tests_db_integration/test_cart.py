from pages.left_menu_component import LeftMenuComponent
from helpers.common_logic import CommonLogic
from pages.products_page import ProductsPage
from pages.header import Header
from pages.cart_page import CartPage
from db.orders_table import get_orders_by_customer_id


class TestCart:
    def test_place_order_check_order_in_db(self, browser, db_connection, delete_orders_of_customer):
        CommonLogic(browser) \
            .login_with_registered_user()

        ProductsPage(browser) \
            .open_list_of_ducks() \
            .add_three_products_to_cart() \
            .open_cart()

        CartPage(browser) \
            .confirm_order()

        orders_count_of_customer = get_orders_by_customer_id(db_connection)

        assert orders_count_of_customer == 1
