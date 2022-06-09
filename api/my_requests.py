import requests
import allure
from api.helpers.serializer import Serializer


class MyRequests:

    base_url = 'https://petstore.swagger.io/v2'

    @staticmethod
    def post(uri: str, headers: dict, data):
        url = f'{MyRequests.base_url}{uri}'
        with allure.step(f'POST request to {url}'):
            return requests.post(url=url, headers=headers, data=Serializer.serialize(data))

    @staticmethod
    def get(uri: str):
        url = f'{MyRequests.base_url}{uri}'
        with allure.step(f'GET request to {url}'):
            return requests.get(url=url)

    @staticmethod
    def delete(uri: str):
        url = f'{MyRequests.base_url}{uri}'
        with allure.step(f'DELETE request to {url}'):
            return requests.delete(url=url)

    @staticmethod
    def put(uri: str, headers: dict, data):
        url = f'{MyRequests.base_url}{uri}'
        with allure.step(f'PUT request to {url}'):
            return requests.put(url=url, headers=headers, data=Serializer.serialize(data))
