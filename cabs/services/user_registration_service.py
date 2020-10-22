from ..exceptions import PassengerRegistrationException
from ..models.address import Address
from ..models.people import Passenger, Driver


class UserRegistrationService:
    @classmethod
    def registerPassenger(self, name: str, address: Address, email: str,
                          phone: str) -> Passenger:
        try:
            passenger = Passenger(name, address, email, phone)
            return passenger
        except Exception:
            raise PassengerRegistrationException()

    @classmethod
    def registerDriver(self, name: str, address: Address, email: str,
                       phone: str, driving_license: str,
                       experience_yrs: int) -> Driver:
        try:
            driver = Driver(name, address, email, phone, driving_license,
                            experience_yrs)
            return driver
        except Exception:
            raise DriverRegistrationException()
