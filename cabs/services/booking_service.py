import logging
from ..db import OPERATING_CITIES
from ..models.address import City
from ..models.people import Passenger
from ..models.booking import Booking
from ..models.vehicle import Vehicle, VehicleStatus
from ..models.trips import Trip
from ..exceptions import CityNotOperationalException, NoCabAvailableException
from .supply_service import SupplyService


class BookingService:
    '''
    Books a cab for a passenger to travel between origin_city
    and dest_city
    @params: passenger, origin_city, dest_city
    @return -> Booking object
    '''
    @classmethod
    def bookVehicle(cls, passenger: Passenger, origin_city: City,
                    dest_city: City) -> Booking:

        if origin_city not in OPERATING_CITIES:
            raise CityNotOperationalException(
                f"Not operational in {origin_city}")

        if dest_city not in OPERATING_CITIES:
            raise CityNotOperationalException(
                f"Not operational in {dest_city}")

        vehicle = SupplyService.selectVehicle(origin_city, dest_city)
        vehicle.bookVehicle()
        logging.info(f"Changed status of vehicle {vehicle} to ON_TRIP")
        if not vehicle or not isinstance(vehicle, Vehicle):
            raise NoCabAvailableException()

        return Booking(passenger, vehicle, origin_city, dest_city)
