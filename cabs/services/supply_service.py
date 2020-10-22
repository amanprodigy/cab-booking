from datetime import datetime
from ..models.vehicle import Vehicle, VehicleStatus
from ..models.address import City
from ..models.people import Passenger
from ..db import CABS, OPERATING_CITIES


class SupplyService:
    @classmethod
    def selectVehicle(cls, origin_city: City, dest_city: City) -> Vehicle:
        for cab in CABS:
            if cab.getCurrentCity() == origin_city and cab.isIdle():
                return cab
        return None

    @classmethod
    def getStatsOfCabsInCity(cls, city) -> int:
        num_idle, num_ontrip = 0, 0
        for cab in CABS:
            if cab.getCurrentCity() == city and cab.isIdle():
                num_idle += 1
            if cab.getCurrentCity() == city and cab.getStatus(
            ) == VehicleStatus.ON_TRIP:
                num_ontrip += 1
        return (num_idle, num_ontrip)

    @classmethod
    def getTotalStatsAcrossOperatingCities(cls):
        stat = {'idles': 0, 'ontrip': 0, 'repairing': 0}
        stats = {city.name: stat for city in OPERATING_CITIES}
        for city in OPERATING_CITIES:
            for cab in CABS:
                if cab.getCurrentCity() == city:
                    if cab.isIdle():
                        stats[city.name]['idles'] += 1
                    if cab.getStatus() == VehicleStatus.ON_TRIP:
                        stats[city.name]['ontrip'] += 1
                    if cab.getStatus() == VehicleStatus.REPAIRING:
                        stats[city.name]['repairing'] += 1
        return stats
