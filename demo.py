import random
from logger import logging
from cabs.models.address import City
from cabs.models.people import Passenger, Driver
from cabs.factories.address_factory import AddressFactory
from cabs.services.booking_service import BookingService
from cabs.services.cab_registration_service import CabRegistrationService
from cabs.services.city_onboarding_service import CityOnboardingService
from cabs.services.user_registration_service import UserRegistrationService
from cabs.services.supply_service import SupplyService
from cabs.db import STATES, CITIES, OPERATING_CITIES, PASSENGESRS, DRIVERS, CABS


class Demo:
    @classmethod
    def run_passenger_registration_demo(self) -> None:
        bangalore = [city for city in CITIES if city.name == 'Bangalore'][0]
        address = AddressFactory.createAddress(bangalore)
        aman = UserRegistrationService.registerPassenger(
            'Aman Srivastava', address, 'aman@xyz.com', '9876543210')
        logging.info(f"Passenger {aman} successfully registered")

    @classmethod
    def run_driver_registration_demo(cls) -> None:
        bangalore = [city for city in CITIES if city.name == 'Bangalore'][0]
        address = AddressFactory.createAddress(bangalore)
        rohit = UserRegistrationService.registerDriver(
            'Rohit Singh',
            address,
            'rohit@xyz.com',
            '8343923201',
            'ABC434232',
            3,
        )
        logging.info(f"Driver {rohit} successfully registered")

    @classmethod
    def show_stats(cls) -> None:
        print('----------CABS STATUS --------------')
        stats = SupplyService.getTotalStatsAcrossOperatingCities()
        logging.info(stats)
        print('-------------------------------')

    @classmethod
    def show_city_stats(cls, city) -> None:
        stats = SupplyService.getStatsOfCabsInCity(city)
        logging.info(
            f"{city} cabs status: Idle: {stats[0]}, OnTrip: {stats[1]}")

    @classmethod
    def run_booking_demo(cls):
        bangalore = [city for city in CITIES if city.name == 'Bangalore'][0]
        mysore = [city for city in CITIES if city.name == 'Mysore'][0]
        logging.info('Stats before booking...')
        print('----------CABS STATUS --------------')
        cls.show_city_stats(bangalore)
        print('----------CABS STATUS --------------')
        bangalore_passengers = [
            p for p in PASSENGESRS if p.getCurrentCity() == bangalore
        ]
        passenger = random.choice(bangalore_passengers)
        # bangalore_cabs = [c for c in CABS if c.city == bangalore]
        booking = BookingService.bookVehicle(passenger, bangalore, mysore)
        logging.info(f"Successfully booked cab: {booking}")
        logging.info('Stats after booking...')
        print('----------CABS STATUS --------------')
        cls.show_city_stats(bangalore)
        print('----------CABS STATUS --------------')

    @classmethod
    def run_demo(cls):
        logging.info('-------- RUNNING DEMO ----------')
        cls.run_passenger_registration_demo()
        cls.run_driver_registration_demo()
        cls.run_booking_demo()
