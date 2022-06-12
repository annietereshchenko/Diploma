import allure
from helpers.common_logic import CommonLogic
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from db.tabels.orders_table import OrdersTable


@allure.epic('Cart')
class TestCart:
    @allure.feature('Orders')
    @allure.description('Placing an order and checking it in DB')
    def test_place_order_check_order_in_db(self, browser, db_connection,
                                           delete_products_from_cart, delete_orders_of_customer):
        CommonLogic(browser) \
            .login_with_registered_user()

        ProductsPage(browser) \
            .open_list_of_products() \
            .add_three_products_to_cart() \
            .open_cart()

        CartPage(browser) \
            .confirm_order()

        orders_count_of_customer = OrdersTable.get_orders_by_customer_id(db_connection)

        assert orders_count_of_customer == 1
