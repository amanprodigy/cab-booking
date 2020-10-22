import random
from .model_factory import ModelFactory
from .address_factory import AddressFactory
from ..models.people import Passenger, Driver, Rating


class PeopleFactory:

    __firstnames = ['Aman', 'Rahul', 'Atul', 'Ankit', 'Mayank']
    __lastnames = ['Srivastava', 'Singh', 'Gupta', 'Raj']
    __domains = ['gmail', 'outlook', 'yahoomail', 'bing']

    @classmethod
    def getName(cls):
        first_name = random.choice(cls.__firstnames)
        last_name = random.choice(cls.__lastnames)
        return f"{first_name} {last_name}"

    @classmethod
    def getEmail(cls, name: str):
        first_name, last_name = name.split()
        domain = random.choice(cls.__domains)
        return f"{first_name.lower()}.{last_name.lower()}@{domain}.com"

    @classmethod
    def getPhone(cls):
        return random.randint(7000000000, 9999999999)

    @classmethod
    def createPassenger(cls, address):
        name = cls.getName()
        email = cls.getEmail(name)
        phone = cls.getPhone()
        return Passenger(name, address, email, phone)

    @classmethod
    def getLicenseNumber(cls):
        return f"ABCD{random.randint(100, 200)}{random.randint(10,99)}"

    @classmethod
    def createDriver(cls, address):
        name = cls.getName()
        email = cls.getEmail(name)
        phone = cls.getPhone()
        driving_license = cls.getLicenseNumber()
        experience_yrs = random.randint(1, 10)
        return Driver(name, address, email, phone, driving_license,
                      experience_yrs)
