from dataclasses import dataclass, field
from typing import Any, Dict
from observer_repository.observer_kit.events import Event

@dataclass(frozen=True)
class ActualizacionSistemaEvento(Event):
    tipo: str
    datos: Dict[str, Any]

    def __post_init__(self):
        if self.tipo == "actualizacion_sistema":
            if 'version' not in self.datos or 'detalles' not in self.datos:
                raise ValueError("Datos incompletos para ActualizacionSistemaEvento: 'version' y 'detalles' son requeridos.")
        elif self.tipo == "destruir":
            if 'razon' not in self.datos:
                raise ValueError("Datos incompletos para ActualizacionSistemaEvento: 'razon' es requerido para tipo 'destruir'.")
        else:
            raise ValueError(f"Tipo de evento no reconocido: {self.tipo}")