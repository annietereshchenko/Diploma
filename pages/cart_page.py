from time import sleep

from helpers.models import Duck
from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators


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
        cast_price = ''.join(filter(lambda c: c.isdigit() or c == '.', price))
        return float(cast_price)

    def remove_products(self):
        self.find_element(CartPageLocators.REMOVE_BUTTON).click()
        return self

    def is_products_card_not_displayed(self):
        return self.is_element_not_visible(CartPageLocators.PRODUCT_FORM)

    def _get_products_table_rows(self):
        html_table = self.find_element(CartPageLocators.PRODUCTS_TABLE)
        items = html_table.find_elements(*CartPageLocators.TAG_TR)
        rows_list = filter(lambda r: not r.get_attribute('class'), items)
        return rows_list

    # ПЕРЕИМЕНОВАТЬ ФУНКЦИИ, ОПРЕДЕЛИТЬСЯ, ЛИБО DUCKS, ЛИБО PRODUCTS

    def get_ducks_from_cart(self):
        rows = self._get_products_table_rows()
        for row in rows:
            if len(row.find_elements(*CartPageLocators.PRODUCT_NAME)) == 0:
                continue
            name = row.find_element(*CartPageLocators.PRODUCT_NAME).text
            price = row.find_element(*CartPageLocators.PRODUCT_PRICE).text
            cast_price = ''.join(filter(lambda c: c.isdigit() or c == '.', price))
            self.ducks_objects_list.append(Duck(name, float(cast_price)))
        return self

    def are_lists_of_products_equal(self, list_od_products_for_adding, list_of_added_products):
        if len(list_od_products_for_adding) != len(list_od_products_for_adding):
            return False
        for item in list_od_products_for_adding:
            if item not in list_of_added_products:
                return False
        return True

    def confirm_order(self):
        self.find_element(CartPageLocators.CONFIRM_BUTTON).click()
        self.wait_until_title_is(CartPageLocators.ORDER_SUCCESS_TITLE)
