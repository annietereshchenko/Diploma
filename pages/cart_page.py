from time import sleep
from helpers.models import Duck
from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators
from helpers.common_logic import CommonLogic


class CartPage(BasePage):
    ducks_objects_list = []

    def change_quantity_of_added_product(self, quantity: int):
        self.clear_input_field_and_send_keys(CartPageLocators.PRODUCT_QUANTITY, str(quantity))
        self.find_element(CartPageLocators.UPDATE_QUANTITY_BUTTON).click()
        # ИЗБАВИТЬСЯ ОТ ЭТОГО КОСТЫЛЯ
        sleep(1)
        return self

    def get_count_of_added_products(self):
        return int(self.get_text_of_element(CartPageLocators.PRODUCT_QUANTITY_IN_TABLE))

    def get_total_price(self):
        price = self.get_text_of_element(CartPageLocators.TOTAL_PRICE)
        return CommonLogic.get_float_price(price)

    def remove_products(self):
        self.find_element(CartPageLocators.REMOVE_BUTTON).click()
        return self

    def is_products_card_not_displayed(self):
        return self.is_element_not_visible(CartPageLocators.PRODUCT_FORM)

    # ПЕРЕИМЕНОВАТЬ ФУНКЦИИ, ОПРЕДЕЛИТЬСЯ, ЛИБО DUCKS, ЛИБО PRODUCTS

    def get_ducks_from_cart(self):
        rows_list = self.find_elements(CartPageLocators.PRODUCTS_TABLE_ROWS)
        list_without_header_footer = filter(lambda r: not r.get_attribute('class'), rows_list)
        for row in list_without_header_footer:
            if len(row.find_elements(*CartPageLocators.PRODUCT_NAME)) == 0:
                continue
            name = row.find_element(*CartPageLocators.PRODUCT_NAME).text
            price = row.find_element(*CartPageLocators.PRODUCT_PRICE).text
            cast_price = CommonLogic.get_float_price(price)
            self.ducks_objects_list.append(Duck(name, cast_price))
        return self

    def are_lists_of_products_equal(self, list_of_products_for_adding, list_of_added_products):
        if len(list_of_products_for_adding) != len(list_of_products_for_adding):
            return False
        for item in list_of_products_for_adding:
            if item not in list_of_added_products:
                return False
        return True

    def confirm_order(self):
        self.find_element(CartPageLocators.CONFIRM_BUTTON).click()
        self.wait_until_title_is(CartPageLocators.ORDER_SUCCESS_TITLE)
