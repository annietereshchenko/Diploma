from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators
from helpers.models import Duck


class ProductPage(BasePage):
    def get_product_price(self):
        price = self.get_text_of_element(ProductPageLocators.PRODUCT_PRICE)
        cast_price = ''.join(filter(lambda c: c.isdigit() or c == '.', price))
        return float(cast_price)
