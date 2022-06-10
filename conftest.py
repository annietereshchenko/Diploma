import pytest
from api.my_requests import MyRequests
from api.helpers import testing_data as TD
from db.litecart_database import get_db_connection
from selenium import webdriver
from db.db_constants import DBConstants
from helpers.testing_data import TestUserData


@pytest.fixture()
def create_pet():
    MyRequests.post('/pet', headers=TD.HEADERS, data=TD.RED_CHIHUAHUA)


@pytest.fixture()
def create_user():
    MyRequests.post('/user', headers=TD.HEADERS, data=TD.USER)


@pytest.fixture()
def delete_pet():
    yield
    MyRequests.delete(f'/pet/{TD.RED_CHIHUAHUA.id}')


@pytest.fixture()
def delete_user():
    yield
    MyRequests.delete(f'/user/{TD.UserData.USERNAME}')


@pytest.fixture()
def delete_user_after_update():
    yield
    MyRequests.delete(f'/user/{TD.UserData.UPDATED_USERNAME}')


@pytest.fixture()
def browser():
    browser = webdriver.Chrome("C:/Users/Admin/PycharmProjects/automationpractice/chromedriver")
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get('http://localhost/litecart/en/')
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def db_connection():
    connection = get_db_connection('127.0.0.1', 'root', '', 'litecart')
    yield connection
    connection.close()


@pytest.fixture()
def revert_user_names(db_connection):
    yield
    cursor = db_connection.cursor()
    update_user_names = f"UPDATE lc_customers SET firstname = '{TestUserData.FIRST_NAME}', " \
                        f"lastname = '{TestUserData.LAST_NAME}' WHERE id={DBConstants.TEST_CUSTOMER_ID}"
    cursor.execute(update_user_names)
    db_connection.commit()


@pytest.fixture()
def delete_orders_of_customer(db_connection):
    yield
    cursor = db_connection.cursor()
    delete_orders = f"DELETE FROM lc_orders WHERE customer_id={DBConstants.TEST_CUSTOMER_ID}"
    cursor.execute(delete_orders)
    db_connection.commit()


@pytest.fixture()
def delete_products_from_cart(db_connection):
    yield
    cursor = db_connection.cursor()
    delete_orders = f"DELETE FROM lc_cart_items WHERE customer_id={DBConstants.TEST_CUSTOMER_ID}"
    cursor.execute(delete_orders)
    db_connection.commit()
