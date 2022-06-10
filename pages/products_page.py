from time import sleep
from helpers.models import Duck
from locators.products_page_locators import ProductsPageLocators
from locators.product_page_locators import ProductPageLocators
from locators.header_locators import HeaderLocators
from pages.left_menu_component import LeftMenuComponent
from pages.header import Header
from helpers.common_logic import CommonLogic


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
        # если будет время, переписать этот костыль
        sleep(1)
        return self

    def add_three_products_to_cart(self):
        for item in range(2, 5):
            product_list = self.find_elements(ProductsPageLocators.PRODUCTS)
            duck = product_list[item]
            duck.click()
            self.add_product_to_cart()
            # если будет время, переписать этот костыль
            sleep(1)
            self.find_element(HeaderLocators.BREAD_CRUMB_RUBBER_DUCKS).click()
        return self

    def open_product(self):
        self.find_elements(ProductsPageLocators.PRODUCTS)[2].click()
        return self
