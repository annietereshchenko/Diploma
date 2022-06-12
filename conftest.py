import pytest
from api.my_requests import MyRequests
from api.helpers import testing_data as TD
from db.litecart_database import get_db_connection
from db.tabels.orders_table import OrdersTable
from db.tabels.cart_items_table import CartItemsTable
from db.tabels.customers_table import CustomerTables
from selenium import webdriver


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
    driver = webdriver.Chrome(executable_path="C:/Users/Admin/PycharmProjects/automationpractice/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get('http://localhost/litecart/en/')
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def db_connection():
    connection = get_db_connection('127.0.0.1', 'root', '', 'litecart')
    yield connection
    connection.close()


@pytest.fixture()
def revert_user_names(db_connection):
    yield
    CustomerTables.revert_user_names(db_connection)


@pytest.fixture()
def delete_orders_of_customer(db_connection):
    OrdersTable.delete_orders_of_customer(db_connection)
    yield
    OrdersTable.delete_orders_of_customer(db_connection)


@pytest.fixture()
def delete_products_from_cart(db_connection):
    CartItemsTable.delete_products_from_cart(db_connection)
    yield
    CartItemsTable.delete_products_from_cart(db_connection)
