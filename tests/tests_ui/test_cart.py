import allure
from helpers.common_logic import CommonLogic
from pages.products_page import ProductsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from helpers.testing_data import TestCartData


@allure.epic('Cart')
class TestCart:
    @allure.story('Add products to cart')
    @allure.description('Adding products to the cart and checking names and prices in the cart')
    def test_add_products_to_cart_check_price_and_name(self, browser, delete_products_from_cart):
        CommonLogic(browser) \
            .login_with_registered_user()

        product_page = ProductsPage(browser) \
            .open_list_of_products() \
            .get_products_in_list() \
            .add_three_products_to_cart()\
            .open_cart()

        cart_page = CartPage(browser) \
            .get_products_in_cart()

        assert cart_page.are_lists_of_products_equal(product_page.products_objects_list,
                                                     cart_page.products_objects_list) is True

    @allure.story('Edit the count of products in cart')
    @allure.description('Changing the count of added products and checking the count in the cart')
    def test_change_count_of_products_check_count(self, browser, delete_products_from_cart):
        CommonLogic(browser) \
            .login_with_registered_user()

        ProductsPage(browser) \
            .open_list_of_products() \
            .open_product() \
            .add_product_to_cart() \
            .open_cart()

        cart_page = CartPage(browser) \
            .change_quantity_of_added_product(TestCartData.QUANTITY_3)

        assert cart_page.get_count_of_added_products() == TestCartData.QUANTITY_3

    @allure.story('Edit the count of products in cart')
    @allure.description('Changing the count of added products and checking the total price')
    def test_change_count_of_products_check_price(self, browser, delete_products_from_cart):
        CommonLogic(browser) \
            .login_with_registered_user()

        products_page = ProductsPage(browser) \
            .open_list_of_products() \
            .open_product() \
            .add_product_to_cart()

        product_price = ProductPage(browser) \
            .get_product_price()

        products_page \
            .open_cart()

        cart_page = CartPage(browser) \
            .change_quantity_of_added_product(TestCartData.QUANTITY_3)

        assert cart_page.get_total_price() == product_price * TestCartData.QUANTITY_3

    @allure.feature('Remove products from cart')
    @allure.description('Removing products and checking that products are not displayed')
    def test_remove_products_check_products_card(self, browser):
        CommonLogic(browser) \
            .login_with_registered_user()

        ProductsPage(browser) \
            .open_list_of_products() \
            .open_product() \
            .add_product_to_cart()\
            .open_cart()

        cart_page = CartPage(browser) \
            .change_quantity_of_added_product(TestCartData.QUANTITY_3) \
            .remove_products()

        assert cart_page.is_products_card_not_displayed() is True

    #def test msg No items
