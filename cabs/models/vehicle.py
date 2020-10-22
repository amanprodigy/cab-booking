from enum import Enum

from .base import Base
from .make import Model
from .address import City


class VehicleStatus(Enum):
    IDLE, ON_TRIP, REPAIRING, TOTALLED, EXITED = 1, 2, 3, 4, 5


class VechicleType(Enum):
    HATCHBACK, SEDAN, MUV, SUV, SALOON, TRAVELLER = 1, 2, 3, 4, 5, 6


class Vehicle(Base):
    def __init__(self,
                 license_num: str,
                 capacity: int,
                 model: Model,
                 vehicle_type: VechicleType,
                 year: int,
                 mileage: float,
                 city: City,
                 status: VehicleStatus = VehicleStatus.IDLE):
        self.__license_number = license_num
        self.__passenger_capacity = capacity
        self.__model = model
        self.__vehicle_type = vehicle_type
        self.__year = year
        self.__mileage = mileage
        self.__city = city
        self.__status = status

    def getStatus(self):
        return self.__status

    def isIdle(self):
        return self.getStatus() == VehicleStatus.IDLE

    def updateStatus(self, status: VehicleStatus):
        self.__status = status

    def bookVehicle(self):
        self.updateStatus(VehicleStatus.ON_TRIP)

    def changeCurrentCity(self, city: City):
        self.__city = city

    def getCurrentCity(self):
        return self.__city

    def __repr__(self):
        return f"{self.__model} {self.__license_number}"
