from selenium.webdriver.common.by import By


class ProductsPageLocators:
    PRODUCTS = (By.CSS_SELECTOR, '.product.column.shadow.hover-light')
    PRODUCT_NAME = (By.CLASS_NAME, 'name')
    PRODUCT_PRICE_WITHOUT_DISCOUNT = (By.CLASS_NAME, 'price')
