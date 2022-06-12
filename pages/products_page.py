from allure_commons._allure import step
from helpers.models import Product
from locators.products_page_locators import ProductsPageLocators
from locators.header_locators import HeaderLocators
from pages.left_menu_component import LeftMenuComponent
from pages.header import Header
from helpers.common_logic import CommonLogic
from pages.product_page import ProductPageLocators


class ProductsPage(LeftMenuComponent, Header):
    products_objects_list = []

    @step('Getting products for adding')
    def get_products_in_list(self):
        products_list = self.find_elements(ProductsPageLocators.PRODUCTS)
        for item in products_list[2:5]:
            name = item.find_element(*ProductsPageLocators.PRODUCT_NAME).text
            price = item.find_element(*ProductsPageLocators.PRODUCT_PRICE_WITHOUT_DISCOUNT).text
            cast_price = CommonLogic.get_float_price(price)
            self.products_objects_list.append(Product(name, cast_price))
        return self

    @step('Add a product to the cart')
    def add_product_to_cart(self):
        count_before_adding_product = self.get_text_of_element(HeaderLocators.COUNTER)
        self.find_element(ProductPageLocators.ADD_TO_CART_BUTTON).click()
        self.wait_until_text_not_present(HeaderLocators.COUNTER, count_before_adding_product)
        return self

    @step('Add three product to cart')
    def add_three_products_to_cart(self):
        for item in range(2, 5):
            product_list = self.find_elements(ProductsPageLocators.PRODUCTS)
            product = product_list[item]
            product.click()
            self.add_product_to_cart()
            self.find_element(HeaderLocators.BREAD_CRUMB_RUBBER_DUCKS).click()
        return self

    @step('Open a product')
    def open_product(self):
        products_list = self.find_elements(ProductsPageLocators.PRODUCTS)
        products_list[2].click()
        return self
