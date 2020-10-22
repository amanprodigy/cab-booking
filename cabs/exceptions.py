class VehicleRegistrationException(Exception):
    message = 'Could not register vehicle'


class CityAlreadyOnboardedException(Exception):
    message = 'This city is already onboarded'


class CityNotOperationalException(Exception):
    message = 'Currently not running operations in this city'


class PassengerRegistrationException(Exception):
    message = 'Unable to register passenger'


class DriverRegistrationException(Exception):
    message = 'Unable to register driver'


class NoCabAvailableException(Exception):
    message = 'No Cabs are available at this time'
