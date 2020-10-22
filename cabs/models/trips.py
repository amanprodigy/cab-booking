from datetime import datetime
from enum import Enum

from .base import Base
from .people import Passenger, Driver
from .vehicle import Vehicle
from .booking import Booking

PER_HOUR_COST = 400
PER_KM_COST = 20


class TripStatus(Enum):
    NOT_STARTED, STARTED, PAUSED, FINISHED, ABORTED = 1, 2, 3, 4, 5


class Trip(Base):
    def __init__(self, booking: Booking, is_return: bool = False):
        super().__init__()
        self.__booking = booking
        self.__is_return = is_return  # forward or return journey
        self.__status = TripStatus.NOT_STARTED

        self.__start_time = None
        self.__end_time = None
        self.__distance_km = 0.0
        self.__cost_estimate = 0.0

    def getBooking(self):
        return self.__booking

    def getDistance(self):
        return self.__distance_km

    def currentStatus(self):
        return self.__status

    def updateStatus(self, status):
        self.__status = status

    def startTrip(self):
        self.__start_time = datetime.utcnow()
        self.updateStatus(TripStatus.STARTED)

    def endTrip(self, distance_km):
        self.__end_time = datetime.utcnow()
        self.updateStatus(TripStatus.FINISHED)
        self.__distance_km = distance_km

    def estimateCost(self):
        if not self.__end_time and not self.__distance_km:
            raise Exception(
                'Cant estimate cost since the trip details not provided')

        # Refactor this to a util
        diff = self.__end_time - self.__start_time
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        cost_by_hour = hours * PER_HOUR_COST
        cost_by_km = self.__distance_km * PER_HOUR_COST
        return max(cost_by_km, cost_by_hour)

    def __repr__(self):
        return f"Trip # {self.getId()}"
