
import asyncio

from observer_repository.observer_kit.events import Event
from observer_repository.observer_kit.observer import Observer

class LogObserver(Observer[Event]):
    async def update(self, event: Event) -> None:
        await self.log_event(event)

    async def log_event(self, event: Event) -> None:

        await asyncio.sleep(0.5)
        print(f"Registrando evento: {event.tipo} con datos {event.datos}")
