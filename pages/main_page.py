from locators.main_page_locators import MainPageLocators
from pages.header import Header
from pages.reqional_settings_popup import RegionalPopup


class MainPage(Header, RegionalPopup):

    def enter_email(self, email):
        self.send_keys(MainPageLocators.EMAIL_FIELD, email)
        return self

    def enter_password(self, password):
        self.send_keys(MainPageLocators.PASSWORD_FIELD, password)
        return self

    def click_on_login_button(self):
        self.find_element(MainPageLocators.LOGIN_BUTTON).click()
        return self

    def get_text_of_welcome_message(self):
        return self.get_text_of_element(MainPageLocators.LOGIN_MESSAGE)
