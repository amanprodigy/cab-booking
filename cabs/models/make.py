from enum import Enum
from .base import Base


class Make(Enum):
    HONDA = 'HONDA',
    HYUNDAI = 'HYUNDAI',
    FORD = 'FORD',
    SUZUKI = 'SUZUKI',
    TOYOTA = 'TOYOTA'


class Model(Base):
    def __init__(self, name: str, make: Make):
        self.__name = name
        self.__make = make

    def __repr__(self):
        return f"{self.__make} {self.__name}"
