from enum import Enum


class Country(Enum):
    INDIA, USA = 'IND', 'USA'


class State(object):
    def __init__(self, name: str, state_code: str, country: Country):
        self.name = name
        self.state_code = state_code
        self.country = country

    def __repr__(self):
        return self.state_code


class City(object):
    def __init__(self, name, state: State):
        self.name = name
        self.state = state

    def __repr__(self):
        return f"{self.name} ({self.state})"


class Address(object):
    def __init__(self, street: str, city: City, zip_code: int):
        self.__street_address = street
        self.__city = city
        self.__zip_code = zip_code

    def getCity(self):
        return self.__city

    def __repr__(self):
        return f"{self.__street_address} {self.__city}"
