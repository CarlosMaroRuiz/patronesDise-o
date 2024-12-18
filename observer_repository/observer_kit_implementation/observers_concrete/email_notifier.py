import asyncio
from observer_repository.observer_kit.observer import Observer
from .. import NuevoUsuarioEvento

class EmailNotifier(Observer[NuevoUsuarioEvento]):
    async def update(self, event: NuevoUsuarioEvento) -> None:
        await self.enviar_email(event.datos)

    async def enviar_email(self, datos: dict) -> None:
        await asyncio.sleep(1) 
        print(f"Enviando email a {datos['email']} sobre {datos['mensaje']}")
