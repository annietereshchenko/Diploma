import allure
from pages.main_page import MainPage
from helpers.testing_data import TestUserData as TD


class CommonLogic(MainPage):
    def login_with_registered_user(self):
        with allure.step('Log in'):
            self.enter_email(TD.EMAIL)\
                .enter_password(TD.PASSWORD)\
                .click_on_login_button()
            return self

    @staticmethod
    def get_float_price(price: str):
        cast_price = ''.join(filter(lambda c: c.isdigit() or c == '.', price))
        return float(cast_price)
