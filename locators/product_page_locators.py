from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.NAME, 'add_cart_product')
    PRODUCT_PRICE = (By.CLASS_NAME, 'price')
    ADD_TO_CART_BUTTON_WITH_CURSOR = (By.CSS_SELECTOR, ".quantity [type='submit'][style='cursor: wait;']")
