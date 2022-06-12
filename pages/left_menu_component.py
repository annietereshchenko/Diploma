from pages.base_page import BasePage
from locators.left_menu_component_locators import LeftMenuComponentLocators


class LeftMenuComponent(BasePage):
    def open_list_of_products(self):
        self.find_element(LeftMenuComponentLocators.PRODUCTS_LIST_LINK).click()
        return self

    def open_account_settings(self):
        self.find_element(LeftMenuComponentLocators.EDIT_ACCOUNT_LINK).click()
        return self
