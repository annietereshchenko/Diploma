from pages.base_page import BasePage
from locators.header_locators import HeaderLocators


class Header(BasePage):
    def open_regional_settings_popup(self):
        self.find_element(HeaderLocators.CHANGE_SETTINGS_BUTTON).click()
        return self

    def get_text_of_country(self):
        return self.get_text_of_element(HeaderLocators.COUNTRY)

    def get_text_of_currency(self):
        return self.get_text_of_element(HeaderLocators.CURRENCY)

    def open_cart(self):
        self.find_element(HeaderLocators.CHECKOUT).click()
        return self
