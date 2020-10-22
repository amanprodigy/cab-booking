from ..exceptions import VehicleRegistrationException, CityNotOperationalException
from ..models.vehicle import Model, VehicleStatus, Vehicle
from ..models.address import City
from ..db import OPERATING_CITIES


class CabRegistrationService:
    @classmethod
    def registerCab(cls, license_num: str, capacity: int,
                    status: VehicleStatus, model: Model, year: str,
                    mileage: float, city: City) -> Vehicle:
        '''
        Registers a new cab in the system and returns the vehicle
        '''
        # quickly exit if not operating in this city
        if city not in OPERATING_CITIES:
            raise CityNotOperationalException

        try:
            vehicle = Vehicle(license_num, capacity, status, model, year,
                              mileage, city)
            return vehicle
        except Exception:
            raise VehicleRegistrationException()
