from selenium.webdriver.common.by import By


class MainPageLocators:
    NEW_CUSTOMER_LINK = (By.LINK_TEXT, 'New customers click here')
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    LOGIN_MESSAGE = (By.CSS_SELECTOR, ".notice.success")

