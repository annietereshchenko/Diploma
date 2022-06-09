import json
from types import SimpleNamespace
import allure


class User:
    def __init__(self, id: int, username: str, first_name: str, last_name: str, email: str,
                 password: str, phone: str, userStatus: int):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus

    def __eq__(self, other):
        return self.id == other.id and self.username == other.username and \
               self.email == other.email and self.password == other.password and \
               self.phone == other.phone and self.userStatus == other.userStatus


class UserResponse:
    def __init__(self, id: int, username: str, email: str,
                 password: str, phone: str, userStatus: int):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus

    @staticmethod
    def deserialize_json(json_str: str):
        obj = json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))
        with allure.step(f'Get user object from response'):
            return UserResponse(obj.id, obj.username, obj.email, obj.password, obj.phone, obj.userStatus)
