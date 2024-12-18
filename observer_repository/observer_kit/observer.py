from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

T = TypeVar('T', bound='Event')

class Observer(ABC, Generic[T]):

    @abstractmethod
    async def update(self, event: T) -> None:

        pass
