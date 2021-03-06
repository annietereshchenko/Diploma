from allure_commons._allure import step
from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators
from helpers.common_logic import CommonLogic


class ProductPage(BasePage):
    @step('Getting a product price')
    def get_product_price(self):
        price = self.get_text_of_element(ProductPageLocators.PRODUCT_PRICE)
        return CommonLogic.get_float_price(price)
