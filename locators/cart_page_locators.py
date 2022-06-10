from selenium.webdriver.common.by import By


class CartPageLocators:
    PRODUCT_QUANTITY = (By.NAME, 'quantity')
    UPDATE_QUANTITY_BUTTON = (By.NAME, 'update_cart_item')
    REMOVE_BUTTON = (By.NAME, 'remove_cart_item')
    TOTAL_PRICE = (By.CSS_SELECTOR, 'td.sum')
    PRODUCT_FORM = (By.NAME, 'cart_form')
    PRODUCT_QUANTITY_IN_TABLE = (By.CSS_SELECTOR, "td[style='text-align: center;']")
    NO_PRODUCTS_TEXT = (By.CSS_SELECTOR, '#checkout-cart-wrapper p em')
    PRODUCTS_TABLE_ROWS = (By.CSS_SELECTOR, '.dataTable.rounded-corners tr')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'td .item')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'td .unit-cost')
    CONFIRM_BUTTON = (By.NAME, 'confirm_order')
    ORDER_SUCCESS_TITLE = 'Order Success | My Store'
