
from typing import Any
from abc import ABC, abstractmethod
class Event(ABC):

    @property
    @abstractmethod
    def type(self) -> str:
        pass

    @property
    @abstractmethod
    def data(self) -> Any:
        pass
