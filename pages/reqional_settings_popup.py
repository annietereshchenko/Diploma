from pages.base_page import BasePage
from locators.regional_settings_popup_locators import RegionalSettingsPopupLocators as RsLocators


class RegionalPopup(BasePage):

    def change_currency(self, value):
        self.select(RsLocators.CURRENCY_SETTINGS, value)
        return self

    def change_country(self, value):
        self.select(RsLocators.COUNTRY_SETTINGS, value)
        return self

    def click_on_save_button(self):
        self.find_element(RsLocators.SAVE_BUTTON).click()
        return self

