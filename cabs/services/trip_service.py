import logging
from ..models.booking import Booking
from ..models.trips import Trip


class TripService:
    '''
    Creates and manages the trips for a booking
    '''
    @classmethod
    def createForwardTrip(cls, booking: Booking) -> Trip:
        return Trip(booking, False)

    @classmethod
    def createReturnTrip(cls, booking: Booking) -> Trip:
        return Trip(booking, False)

    @classmethod
    def startTrip(cls, trip: Trip) -> None:
        trip.startTrip()
        logging.info(f"{trip} started")

    @classmethod
    def endTrip(cls, trip: Trip, distance_km: float) -> None:
        if not distance_km:
            raise Exception('Distance travelled required to end trip')
        trip.endTrip(distance_km)
        logging.info(f"{trip} ended")

    @classmethod
    def estimateCost(cls, trip) -> float:
        return trip.estimateCost()
