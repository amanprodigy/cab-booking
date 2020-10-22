from enum import Enum
from .address import Address
from .base import Base


class Rating(Enum):
    UNRATED, ONE, TWO, THREE, FOUR, FIVE = 0, 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5


class Person(Base):
    def __init__(self, name: str, address: Address, email: str, phone: str):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = AccountStatus.ACTIVE

    def getAddress(self):
        return self.__address

    def getCurrentCity(self):
        return self.getAddress()

    def __repr__(self):
        return f"{self.__name} <{self.__email} {self.__phone}>"


class Passenger(Person):
    def __init__(self, name: str, address: Address, email: str, phone: str):
        super().__init__(name, address, email, phone)
        self.__rating = Rating.UNRATED


class Driver(Person):
    def __init__(self, name: str, address: Address, email: str, phone: str,
                 driving_license: str, experience_yrs: int):
        super().__init__(name, address, email, phone)
        self.__driving_license = driving_license
        self.__experience_yrs = experience_yrs
        self.__rating = Rating.UNRATED
