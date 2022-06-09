from api.models.pet import Pet
from api.helpers import testing_data as TD
from api.my_requests import MyRequests
from api.assertions import Assertions

import allure


@allure.epic('Pet')
class TestPet:
    @allure.feature('Create a pet')
    @allure.story('Create a pet with correct data')
    def test_add_pet_check_status_code(self, delete_pet):
        add_pet_response = MyRequests.post('/pet', headers=TD.HEADERS, data=TD.RED_CHIHUAHUA)
        Assertions.assert_code_status(add_pet_response, 200)

    @allure.feature('Create a pet')
    @allure.story('Create a pet with correct data')
    def test_add_pet_check_added_pet(self, create_pet, delete_pet):
        get_pet_response = MyRequests.get(f'/pet/{TD.RED_CHIHUAHUA.id}')
        added_pet_object = Pet.deserialize_json(get_pet_response.text)
        Assertions.assert_objects_equality(TD.RED_CHIHUAHUA, added_pet_object)

    @allure.feature('Delete a pet')
    def test_delete_pet_check_status(self, create_pet):
        delete_pet_response = MyRequests.delete(f'/pet/{TD.RED_CHIHUAHUA.id}')
        Assertions.assert_code_status(delete_pet_response, 200)

    @allure.feature('Delete a pet')
    def test_delete_pet_get_deleted_pet(self, create_pet):
        MyRequests.delete(f'/pet/{TD.RED_CHIHUAHUA.id}')
        get_pet_response = MyRequests.get(f'/pet/{TD.RED_CHIHUAHUA.id}')
        Assertions.assert_code_status(get_pet_response, 404)
