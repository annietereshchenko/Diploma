from api.models.category import Category
from api.models.tag import Tag
from api.models.pet import Pet
from api.models.user import User


class Status:
    AVAILABLE_STATUS = 'available'
    BOOKED_STATUS = 'pending'
    SOLD_STATUS = 'sold'


class CategoryNames:
    DOG = 'dog'
    CAT = 'cat'


class DogBreedTags:
    CHIHUAHUA = 'chihuahua'
    GSD = 'gsd'


class CatBreedTags:
    BRITISH = 'british'


class ColorTag:
    BLACK = 'black'
    WHITE = 'white'
    RED = 'red'


class PhotoUrls:
    RED_CHIHUAHUA_PHOTO_URL = 'https://previews.123rf.com/images/rodrusoleg/rodrusoleg1307/' \
                              'rodrusoleg130700030/20841380-red-chihuahua-dog-sits-on-a-granite' \
                              '-pedestal-sele%C3%B1%20tive-focus-.jpg'
    GREY_BRITISH_CAT_PHOTO_URL = 'https://www.thesprucepets.com/thmb/ZW8v-2C7IU2c0e7OHgHee3d_J8o=/' \
                                 '2121x1414/filters:fill(auto,1)/GettyImages-1319774380-c' \
                                 '3da91f9259a47e0966007f8e10690ba.jpg'


dog_category = Category(id=1, name=CategoryNames.DOG)

dog_breed_tag = Tag(id=1, name=DogBreedTags.CHIHUAHUA)
red_color_tag = Tag(id=2, name=ColorTag.RED)

RED_CHIHUAHUA = Pet(id=1331, category=dog_category, name='tapochka',
                    photoUrls=[PhotoUrls.RED_CHIHUAHUA_PHOTO_URL],
                    tags=[dog_breed_tag, red_color_tag], status=Status.BOOKED_STATUS)

HEADERS = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'api-key': 'special-key'
    }


class UserData:
    ID = 2000
    USERNAME = 'annie'
    UPDATED_USERNAME = 'Hanna'
    FIRST_NAME = 'Anna'
    LAST_NAME = 'Tereshchenko'
    EMAIL = 'a@email.com'
    PASSWORD = '1234'
    PHONE = '+375299989923'
    USER_STATUS = 1


USER = User(UserData.ID, UserData.USERNAME, UserData.FIRST_NAME, UserData.LAST_NAME,
            UserData.EMAIL, UserData.PASSWORD, UserData.PHONE, UserData.USER_STATUS)

UPDATED_USER = User(UserData.ID, UserData.UPDATED_USERNAME, UserData.FIRST_NAME, UserData.LAST_NAME,
                    UserData.EMAIL, UserData.PASSWORD, UserData.PHONE, UserData.USER_STATUS)
