import random
from ..models.vehicle import Vehicle, VechicleType, VehicleStatus
from ..models.address import City
from .model_factory import ModelFactory


class VehicleFactory:
    __data = ['Ford', 'Figo', '2004', 'ABC0001']

    @classmethod
    def getLicenseNumber(cls, state):
        return f"{state.state_code}{random.randint(10,99)}{cls.getYear()}"

    @classmethod
    def getYear(cls):
        return random.randint(1990, 2020)

    @classmethod
    def chooseModel(cls):
        return ModelFactory.createModel()

    @classmethod
    def createVehicle(cls, city: City, vehicle_status: VehicleStatus):
        license_num = cls.getLicenseNumber(city.state)
        capacity = random.randint(1, 4)
        model = cls.chooseModel()
        vehicle_type = random.randint(1, 6)
        year = cls.getYear()
        mileage = random.randint(100, 100000)
        return Vehicle(license_num, capacity, model, vehicle_type, year,
                       mileage, city, vehicle_status)
