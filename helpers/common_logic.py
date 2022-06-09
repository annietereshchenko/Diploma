from pages.main_page import MainPage
from helpers.testing_data import TestUserData as TD


class CommonLogic(MainPage):
    def login_with_registered_user(self):
        self.enter_email(TD.EMAIL)\
            .enter_password(TD.PASSWORD)\
            .click_on_login_button()
        return self


