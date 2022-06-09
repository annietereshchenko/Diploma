from selenium.webdriver.common.by import By


class AccountCartPageLocators:
    FIRST_NAME = (By.NAME, 'firstname')
    LAST_NAME = (By.NAME, 'lastname')
    SAVE_BUTTON = (By.NAME, 'save')
    