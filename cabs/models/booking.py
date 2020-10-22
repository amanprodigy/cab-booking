from datetime import datetime
from enum import Enum

from .base import Base
from .address import City
from .people import Passenger, Driver
from .vehicle import Vehicle

# DATEFORMAT = f"%d-%m-%Y %H:%M"


class BookingStatus(Enum):
    CONFIRMED, PENDING, COMPLETED, CANCELLED = 1, 2, 3, 4


class Booking(Base):
    def __init__(
            self,
            # booked_from: datetime, booked_till: datetime,
            passenger: Passenger,
            vehicle: Vehicle,
            origin_city: City,
            dest_city: City):
        super().__init__()
        # self.__booked_from = booked_from
        # self.__booked_till = booked_till
        self.__passenger = passenger
        self.__vehicle = vehicle
        self.__booking_status = BookingStatus.CONFIRMED
        self.__origin_city = origin_city
        self.__dest_city = dest_city
        self.__driver = None  # driver can be assigned later

    def updateStatus(self, status: BookingStatus) -> None:
        self.__booking_status = status

    def getStatus(self) -> BookingStatus:
        return self.__booking_status

    def cancelBooking(self) -> None:
        # Completed Bookings cannot be cancelled
        if self.__booking_status != BookingStatus.COMPLETED:
            self.updateStatus(BookingStatus.CANCELLED)

    def bookedAt(self) -> datetime:
        return self.__created_at

    # def bookedFrom(self) -> datetime:
    #     return self.__booked_from.strftime(DATEFORMAT)

    # def bookedTill(self) -> datetime:
    #     return self.__booked_till.strftime(DATEFORMAT)

    def getPassenger(self) -> Passenger:
        return self.__passenger

    def getVehicle(self) -> Vehicle:
        return self.__vehicle

    def assignDriver(self, driver: Driver) -> None:
        self.__driver = driver

    def getDriver(self) -> Driver:
        return self.__driver

    def __repr__(self):
        return f"Booking#{self.getId()} {self.__vehicle} {self.__passenger} "
