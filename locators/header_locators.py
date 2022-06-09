from selenium.webdriver.common.by import By


class HeaderLocators:
    CHANGE_SETTINGS_BUTTON = (By.CLASS_NAME, 'change')
    CURRENCY = (By.CLASS_NAME, 'currency')
    COUNTRY = (By.CLASS_NAME, 'country')
    CHECKOUT = (By.LINK_TEXT, 'Checkout »')
    BREAD_CRUMB_RUBBER_DUCKS = (By.LINK_TEXT, 'Rubber Ducks')
    ADDED_PRODUCTS_QUANTITY = (By.CSS_SELECTOR, '#cart > a.content > span.quantity')
