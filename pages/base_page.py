from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_element(self, locator, timeout=15):
        element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator, timeout=15):
        elements = WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def is_element_not_visible(self, locator, timeout=15):
        elements = WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))
        return elements

    def send_keys(self, locator, keys):
        element = self.find_element(locator)
        element.send_keys(keys)

    def get_text_of_element(self, locator):
        element = self.find_element(locator)
        return element.text

    def select(self, locator, value):
        Select(self.find_element(locator)).select_by_value(value)

    def clear_input_field_and_send_keys(self, locator, keys):
        element = self.find_element(locator)
        element.clear()
        self.send_keys(locator, keys)

    def wait_until_title_is(self, title, timeout=5):
        WebDriverWait(self.browser, timeout).until(EC.title_is(title))

    def wait_until_text_not_present(self, locator, text):
        WebDriverWait(self.browser, 10).until_not(EC.text_to_be_present_in_element(locator, text))
