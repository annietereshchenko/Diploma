from selenium.webdriver.common.by import By


class RegionalSettingsPopupLocators:
    CURRENCY_SETTINGS = (By.NAME, 'currency_code')
    COUNTRY_SETTINGS = (By.NAME, 'country_code')
    SAVE_BUTTON = (By.NAME, 'save')

