from ..exceptions import CityAlreadyOnboardedException
from ..db import OPERATING_CITIES
from ..models.address import City


class CityOnboardingService:
    @classmethod
    def onboardCity(cls, city: City) -> None:
        if city in OPERATING_CITIES:
            raise CityAlreadyOnboardedException()
        OPERATING_CITIES.append(city)
