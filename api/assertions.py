from requests import Response
import allure


class Assertions:

    @staticmethod
    def assert_code_status(response: Response, expected_status):
        with allure.step(f'Check status code'):
            assert response.status_code == expected_status, \
                f"Unexpected status code. Expected {expected_status}, got {response.status_code}, {response.text}"

    @staticmethod
    def assert_objects_equality(object1, object2):
        with allure.step(f'Compare added object and object from response'):
            assert (object1 == object2) is True
