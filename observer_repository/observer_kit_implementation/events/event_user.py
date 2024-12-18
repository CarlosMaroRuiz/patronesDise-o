from dataclasses import field, dataclass
from typing import Dict, Any
from observer_repository.observer_kit.events import Event


@dataclass(frozen=True)
class NuevoUsuarioEvento(Event):
    tipo: str = field(init=False, default="nuevo_usuario")
    datos: Dict[str, Any]

    def __post_init__(self):
        if 'email' not in self.datos or 'mensaje' not in self.datos:
            raise ValueError("Datos incompletos para NuevoUsuarioEvento: 'email' y 'mensaje' son requeridos.")

    def type(self) -> str:
        return self.tipo

    def data(self) -> Dict[str, Any]:
        return self.datos

