import allure
from pages.left_menu_component import LeftMenuComponent
from helpers.common_logic import CommonLogic
from pages.products_page import ProductsPage
from pages.product_page import ProductPage
from pages.header import Header
from pages.cart_page import CartPage
from helpers.testing_data import TestCartData
from db.orders_table import get_orders_by_customer_id


class TestCart:
    def test_add_products_to_cart_check_price_and_name(self, browser, delete_products_from_cart):
        CommonLogic(browser) \
            .login_with_registered_user()

        LeftMenuComponent(browser) \
            .open_list_of_ducks()

        product_page = ProductsPage(browser) \
            .get_ducks_in_list() \
            .add_three_products_to_cart()

        Header(browser) \
            .open_cart()

        cart_page = CartPage(browser) \
            .get_ducks_from_cart()

        assert cart_page.are_lists_of_products_equal(product_page.ducks_objects_list,
                                                     cart_page.ducks_objects_list) is True

    def test_place_order(self, browser, db_connection, delete_orders_of_customer):
        CommonLogic(browser) \
            .login_with_registered_user()

        LeftMenuComponent(browser) \
            .open_list_of_ducks()

        ProductsPage(browser) \
            .add_three_products_to_cart()

        Header(browser) \
            .open_cart()

        CartPage(browser) \
            .confirm_order()

        orders_count_of_customer = get_orders_by_customer_id(db_connection)

        assert orders_count_of_customer == 1

    def test_add_change_count_of_products_check_count(self, browser, delete_products_from_cart):
        CommonLogic(browser) \
            .login_with_registered_user()

        ProductsPage(browser) \
            .open_product() \
            .add_product_to_cart()

        Header(browser) \
            .open_cart()

        cart_page = CartPage(browser) \
            .change_quantity_of_added_product(TestCartData.QUANTITY_3)

        assert cart_page.get_count_of_added_products() == TestCartData.QUANTITY_3

    def test_add_change_count_of_products_check_price(self, browser, delete_products_from_cart):
        CommonLogic(browser) \
            .login_with_registered_user()

        ProductsPage(browser) \
            .open_product() \
            .add_product_to_cart()

        product_price = ProductPage(browser) \
            .get_product_price()

        Header(browser) \
            .open_cart()

        cart_page = CartPage(browser) \
            .change_quantity_of_added_product(TestCartData.QUANTITY_3)

        assert cart_page.get_total_price() == product_price * TestCartData.QUANTITY_3

    def test_remove_products_check_products_card(self, browser):
        CommonLogic(browser) \
            .login_with_registered_user()

        LeftMenuComponent(browser) \
            .open_list_of_ducks()

        ProductsPage(browser) \
            .open_product() \
            .add_product_to_cart()

        Header(browser) \
            .open_cart()

        cart_page = CartPage(browser) \
            .change_quantity_of_added_product(TestCartData.QUANTITY_3) \
            .remove_products()

        assert cart_page.is_products_card_not_displayed() is True

    #def test msg No items