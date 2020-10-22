import random
from ..models.make import Make


class ModelFactory:
    __makes = [
        Make.HONDA,
        Make.HYUNDAI,
        Make.FORD,
        Make.SUZUKI,
        Make.TOYOTA,
    ]
    __data = {
        Make.HONDA: ['CITY', 'BRV', 'CRV', 'JAZZ'],
        Make.HYUNDAI: ['SONATA', 'CRETA', 'GETZ', 'VERNA'],
        Make.FORD: [
            'FIGO',
            'ECOSPORT',
            'ENDEAVOUR',
        ],
        Make.SUZUKI: [
            'SWIFT',
            'BALENO',
            'ALTO',
        ],
        Make.TOYOTA: [
            'COROLLA',
            'FORTUNER',
        ]
    }

    @classmethod
    def getMake(cls):
        return random.choice(cls.__makes)

    @classmethod
    def createModel(cls):
        model_choices = cls.__data[cls.getMake()]
        model_name = random.choice(model_choices)
        return model_name
