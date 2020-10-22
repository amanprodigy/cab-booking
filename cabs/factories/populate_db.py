import logging
import random
from ..db import STATES, CITIES, OPERATING_CITIES, DRIVERS, PASSENGESRS, CABS
from ..models.vehicle import VehicleStatus
from .address_factory import AddressFactory
from .vehicle_factory import VehicleFactory
from .model_factory import ModelFactory
from .people_factory import PeopleFactory


def populate_db():

    logging.info('------------- Populating DB ---------------')
    logging.info('Populating cities and states...')
    # populate cities and states
    for state in AddressFactory.createStates():

        # add state to db
        STATES.append(state)
        logging.info(f"Created state {state}")

        # create city in this state
        for _ in range(15):
            _city = AddressFactory.createCity(state)
            if _city.name in ['Bangalore', 'Mysore', 'Hyderabad']:
                # only operating in Bangalore, Mysore and Hyderabad
                if _city.name not in [c.name for c in OPERATING_CITIES]:
                    logging.info(f"Added city {_city} in OPERATING_CITIES")
                    OPERATING_CITIES.append(_city)

            if _city.name not in [c.name for c in CITIES]:
                logging.info(f"Added city {_city} in CITIES")
                CITIES.append(_city)

    logging.info('Populating cabs in operating cities...')
    # populate cabs
    for city in OPERATING_CITIES:
        # Create 10 cabs in each operating city
        for _ in range(50):
            status = random.choice([VehicleStatus.IDLE, VehicleStatus.ON_TRIP])
            cab = VehicleFactory.createVehicle(city, status)
            logging.info(f"Created cab {cab} in {city}")
            CABS.append(cab)

    logging.info('Populating drivers and passengers...')
    for city in CITIES:
        # populate passengers
        for _ in range(10):
            _passenger = PeopleFactory.createPassenger(city)
            logging.info(f"Created passenger {_passenger} in {city}")
            PASSENGESRS.append(_passenger)

        # populate drivers
        for _ in range(10):
            _driver = PeopleFactory.createDriver(city)
            logging.info(f"Created driver {_driver} in {city}")
            DRIVERS.append(_driver)
