from dataclasses import dataclass, field
from typing import Any, Dict
from observer_repository.observer_kit.events import Event


@dataclass(frozen=True)
class CompraRealizadaEvento(Event):
    tipo: str = field(init=False, default="compra_realizada")
    datos: Dict[str, Any]

    def __post_init__(self):
        if 'usuario' not in self.datos or 'monto' not in self.datos:
            raise ValueError("Datos incompletos para CompraRealizadaEvento: 'usuario' y 'monto' son requeridos.")

    def type(self) -> str:
        return self.tipo

    def data(self) -> Dict[str, Any]:
        return self.datos
