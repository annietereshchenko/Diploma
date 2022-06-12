from allure_commons._allure import step
from pages.base_page import BasePage
from locators.regional_settings_popup_locators import RegionalSettingsPopupLocators as RsLocators


class RegionalPopup(BasePage):
    @step('Change currency')
    def change_currency(self, value):
        self.select(RsLocators.CURRENCY_SETTINGS, value)
        return self

    @step('Change country')
    def change_country(self, value):
        self.select(RsLocators.COUNTRY_SETTINGS, value)
        return self

    @step('Click on Save button')
    def click_on_save_button(self):
        self.find_element(RsLocators.SAVE_BUTTON).click()
        return self
