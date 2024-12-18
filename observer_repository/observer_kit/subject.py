from typing import List
import asyncio

from .events import Event
from .observer import Observer


class Subject:


    def __init__(self):
        self._observers: List[Observer] = []
        self._lock = asyncio.Lock()

    async def register_observer(self, observer: Observer) -> None:
        async with self._lock:
            if observer not in self._observers:
                self._observers.append(observer)

    async def unregister_observer(self, observer: Observer) -> None:
        async with self._lock:
            if observer in self._observers:
                self._observers.remove(observer)

    async def notify_observers(self, event: Event) -> None:

        async with self._lock:
            observers_snapshot = list(self._observers)
        tasks = []
        for observer in observers_snapshot:
            task = asyncio.create_task(self._safe_notify(observer, event))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)

    async def _safe_notify(self, observer: Observer, event: Event) -> None:

        try:
            await observer.update(event)
        except Exception as e:

            print(f"Error al notificar al observer {observer}: {e}")

