from api.helpers.testing_data import HEADERS, UserData, USER, UPDATED_USER
from api.my_requests import MyRequests
from api.assertions import Assertions
from api.models.user import UserResponse
import allure


@allure.epic('User')
class TestUser:

    @allure.feature('Create a user')
    @allure.story('Create a user with correct data')
    def test_add_user_check_status(self, delete_user):
        add_user_response = MyRequests.post('/user', headers=HEADERS, data=USER)
        Assertions.assert_code_status(add_user_response, 200)

    @allure.feature('Create a user')
    @allure.story('Create a user with correct data')
    def test_add_user_check_added_user(self, create_user, delete_user):
        get_user_response = MyRequests.get(f'/user/{UserData.USERNAME}')
        added_user_object = UserResponse.deserialize_json(get_user_response.text)
        Assertions.assert_objects_equality(USER, added_user_object)

    @allure.feature('Update a user')
    @allure.story('Update a user with correct data')
    def test_update_username_check_status_code(self, create_user, delete_user_after_update):
        put_user_response = MyRequests.put(f'/user/{UserData.USERNAME}', headers=HEADERS, data=UPDATED_USER)
        Assertions.assert_code_status(put_user_response, 200)

    @allure.feature('Update a user')
    @allure.story('Update a user with correct data')
    def test_update_username_check_updated_user(self, create_user, delete_user_after_update):
        MyRequests.put(f'/user/{UserData.USERNAME}', headers=HEADERS, data=UPDATED_USER)
        get_user_response = MyRequests.get(f'/user/{UserData.UPDATED_USERNAME}')
        updated_user_object = UserResponse.deserialize_json(get_user_response.text)
        Assertions.assert_objects_equality(UPDATED_USER, updated_user_object)
