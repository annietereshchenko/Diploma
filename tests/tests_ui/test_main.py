import allure
from pages.main_page import MainPage
from helpers.testing_data import TestDataSettings, TestUserData


@allure.epic('Main')
class TestMain:
    @allure.feature('Regional settings')
    @allure.story('Edit currency')
    @allure.description('Changing the currency and checking that it changes')
    def test_change_currency(self, browser):
        main_page = MainPage(browser) \
            .open_regional_settings_popup() \
            .change_currency(TestDataSettings.EUR_CURRENCY) \
            .click_on_save_button()

        assert main_page.get_text_of_currency() == TestDataSettings.EUR_CURRENCY

    @allure.feature('Regional settings')
    @allure.story('Edit country')
    @allure.description('Changing the country and checking that it changes')
    def test_change_country(self, browser):
        main_page = MainPage(browser) \
            .open_regional_settings_popup() \
            .change_country(TestDataSettings.BELARUS_COUNTRY_CODE) \
            .click_on_save_button()

        assert main_page.get_text_of_country() == TestDataSettings.BELARUS

    @allure.feature('Log in')
    @allure.story('Login with registered user')
    def test_login(self, browser):
        main_page = MainPage(browser) \
            .enter_email(TestUserData.EMAIL) \
            .enter_password(TestUserData.PASSWORD) \
            .click_on_login_button()

        assert main_page.get_text_of_welcome_message() == TestUserData.LOGIN_MESSAGE
