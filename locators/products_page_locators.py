from selenium.webdriver.common.by import By


class ProductsPageLocators:
    PRODUCTS = (By.CSS_SELECTOR, '.product.column.shadow.hover-light')
    PRODUCTS_LIST = (By.CSS_SELECTOR, '.listing-wrapper.products')
    TAG = (By.TAG_NAME, 'li')
    PRODUCT_NAME = (By.CLASS_NAME, 'name')
    PRODUCT_PRICE_WITHOUT_DISCOUNT = (By.CLASS_NAME, 'price')
