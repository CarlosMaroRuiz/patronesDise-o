from observer_repository.observer_kit.observer import Observer
from observer_repository.observer_kit.subject import Subject
from observer_repository.observer_kit_implementation import ActualizacionSistemaEvento


class CustomObserver(Observer[ActualizacionSistemaEvento]):
    def __init__(self, name: str, subject: Subject):
        self.name = name
        self.subject = subject

    async def update(self, event: ActualizacionSistemaEvento) -> None:
        print(f"{self.name}: Evento {event.tipo} recibido con datos {event.datos}")
        if event.tipo == "destruir":
            await self.subject.unregister_observer(self)
            print(f"{self.name}: Desregistrado después de recibir el evento 'destruir'.")
