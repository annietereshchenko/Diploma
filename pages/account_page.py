import allure

from locators.account_page_locators import AccountCartPageLocators
from pages.left_menu_component import LeftMenuComponent


class AccountPage(LeftMenuComponent):

    def edit_first_name(self, first_name: str):
        with allure.step('Edit first name'):
            self.clear_input_field_and_send_keys(AccountCartPageLocators.FIRST_NAME, first_name)
            return self

    def edit_last_name(self, last_name: str):
        with allure.step('Edit last name'):
            self.clear_input_field_and_send_keys(AccountCartPageLocators.LAST_NAME, last_name)
            return self

    def click_on_save_button(self):
        with allure.step('Click on Save button'):
            self.find_element(AccountCartPageLocators.SAVE_BUTTON).click()
            return self
