import allure
from pages.account_page import AccountPage
from db.tabels.customers_table import CustomerTables
from helpers.common_logic import CommonLogic
from helpers.testing_data import TestUserData


@allure.epic('Account')
class TestAccount:
    @allure.feature('Edit a user')
    @allure.description('Editing the first and the last names and checking the changes in DB')
    def test_change_name(self, browser, db_connection, revert_user_names):
        CommonLogic(browser). \
            login_with_registered_user()

        AccountPage(browser) \
            .open_account_settings() \
            .edit_first_name(TestUserData.EDITED_FIRST_NAME) \
            .edit_last_name(TestUserData.EDITED_LAST_NAME) \
            .click_on_save_button()

        names_in_database = CustomerTables.get_test_user_names_by_id(db_connection=db_connection)

        assert names_in_database == (TestUserData.EDITED_FIRST_NAME, TestUserData.EDITED_LAST_NAME)
