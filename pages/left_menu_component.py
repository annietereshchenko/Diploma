from allure_commons._allure import step
from pages.base_page import BasePage
from locators.left_menu_component_locators import LeftMenuComponentLocators


class LeftMenuComponent(BasePage):
    @step('Open list of products')
    def open_list_of_products(self):
        self.find_element(LeftMenuComponentLocators.PRODUCTS_LIST_LINK).click()
        return self

    @step('Open account settings')
    def open_account_settings(self):
        self.find_element(LeftMenuComponentLocators.EDIT_ACCOUNT_LINK).click()
        return self
