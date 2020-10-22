from abc import ABC
from datetime import datetime
from uuid import uuid4, UUID


class TimeTracker(ABC):
    def __init__(self):
        self.__created_at = datetime.utcnow()
        self.__updated_at = datetime.utcnow()


class Base(TimeTracker):
    __id: UUID

    def __init__(self):
        super().__init__()
        self.__id = uuid4()

    def getId(self):
        return self.__id
