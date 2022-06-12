from types import SimpleNamespace
import json
from api.models.category import Category
import allure


def _tags_compare(tags_list_1: list, tags_list_2: list):
    if len(tags_list_1) != len(tags_list_2):
        return False
    tags_list_1 = sorted(tags_list_1, key=lambda x: x.id)
    tags_list_2 = sorted(tags_list_2, key=lambda x: x.id)
    filtered_list = filter(lambda x: (x[0].id != x[1].id or x[0].name != x[1].name), zip(tags_list_1, tags_list_2))
    return len(list(filtered_list)) == 0


def _photo_compare(list1: list, list2: list):
    if len(list1) != len(list2):
        return False
    list1 = sorted(list1)
    list2 = sorted(list2)
    filtered_list = filter(lambda x: (x[0] != x[1]), zip(list1, list2))
    return len(list(filtered_list)) == 0


class Pet:
    def __init__(self, id: int, category: Category, name: str, photoUrls: list, tags: list, status: str):
        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photoUrls
        self.tags = tags
        self.status = status

    def __eq__(self, other):
        is_tags_equal = _tags_compare(self.tags, other.tags)
        is_photo_equal = _photo_compare(self.photoUrls, other.photoUrls)
        return self.id == other.id and self.name == other.name and \
               self.status == other.status and self.category.name == other.category.name and \
               self.category.id == other.category.id and is_tags_equal and is_photo_equal

    @staticmethod
    def deserialize_json(json_str: str):
        obj = json.loads(json_str, object_hook=lambda d: SimpleNamespace(**d))
        with allure.step(f'Get pet object from response'):
            return Pet(obj.id, obj.category, obj.name, obj.photoUrls, obj.tags, obj.status)
