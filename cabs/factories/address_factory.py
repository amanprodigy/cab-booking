import random
from .model_factory import ModelFactory
from ..models.address import Country, State, Address, City


class AddressFactory:
    __data = [
        ['Karnataka', 'KA'],
        ['Andhra Pradesh', 'AP'],
        ['Uttar Pradesh', 'UP'],
        ['Delhi', 'DL'],
        ['Tamil Nadu', 'TL'],
    ]
    __city_data = {
        'KA': [
            'Bangalore',
            'Mysore',
        ],
        'AP': ['Hyderabad', 'Secundarabad'],
        'UP': ['Noida', 'Ghaziabad'],
        'DL': [
            'New Delhi',
            'Delhi',
        ],
        'TL': ['Chennai', 'Kodaikanal'],
    }

    @classmethod
    def createState(cls, obj):
        return State(obj[0], obj[1], Country.INDIA)

    @classmethod
    def createStates(cls):
        output = []
        for _state_data in cls.__data:
            output.append(cls.createState(_state_data))
        return output

    @classmethod
    def createCity(cls, state: State):
        state_code = state.state_code
        city_name = random.choice(cls.__city_data[state_code])
        return City(city_name, state)

    @classmethod
    def getStreetAddress(cls):
        lane = random.randint(1, 100)
        sector = random.randint(1, 100)
        street = f"Lane {lane}, Sector {sector}"
        return street

    @classmethod
    def getZipCode(cls):
        return random.randint(10000, 70000)

    @classmethod
    def createAddress(cls, city: City):
        street = cls.getStreetAddress()
        zip_code = cls.getZipCode()
        return Address(street, city, zip_code)
