from helpers.models import Duck
from locators.products_page_locators import ProductsPageLocators
from locators.header_locators import HeaderLocators
from pages.left_menu_component import LeftMenuComponent
from pages.header import Header
from helpers.common_logic import CommonLogic
from pages.product_page import ProductPageLocators


class ProductsPage(LeftMenuComponent, Header):
    ducks_objects_list = []

    def get_ducks_in_list(self):
        ducks_list = self.find_elements(ProductsPageLocators.PRODUCTS)
        for item in ducks_list[2:5]:
            name = item.find_element(*ProductsPageLocators.PRODUCT_NAME).text
            price = item.find_element(*ProductsPageLocators.PRODUCT_PRICE_WITHOUT_DISCOUNT).text
            cast_price = CommonLogic.get_float_price(price)
            duck = Duck(name, cast_price)
            self.ducks_objects_list.append(duck)
        return self

    # ПЕРЕИМЕНОВАТЬ ФУНКЦИИ, ОПРЕДЕЛИТЬСЯ, ЛИБО DUCKS, ЛИБО PRODUCTS

    def add_product_to_cart(self):
        self.find_element(ProductPageLocators.ADD_TO_CART_BUTTON).click()
        self.wait_until_element_visible(ProductPageLocators.ADD_TO_CART_BUTTON_WITH_CURSOR)
        self.wait_until_element_invisible(ProductPageLocators.ADD_TO_CART_BUTTON_WITH_CURSOR)
        return self

    def add_three_products_to_cart(self):
        for item in range(2, 5):
            product_list = self.find_elements(ProductsPageLocators.PRODUCTS)
            duck = product_list[item]
            duck.click()
            self.add_product_to_cart()
            self.find_element(HeaderLocators.BREAD_CRUMB_RUBBER_DUCKS).click()
        return self

    def open_product(self):
        products_list = self.find_elements(ProductsPageLocators.PRODUCTS)
        products_list[2].click()
        return self
