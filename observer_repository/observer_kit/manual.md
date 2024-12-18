# Uso de ObserverKit

**ObserverKit** esta diseñada para implementar el **Patrón Observer** en  proyectos de Python. Proporciona componentes modulares que facilitan la suscripción y notificación de observadores, soportando tanto operaciones **síncronas** como **asíncronas**.

## Tabla de Contenidos

1. [Clase Subject](#clase-subject)
    - [Descripción](#descripción)
    - [Métodos](#métodos)
        - [`register_observer`](#register_observer)
        - [`unregister_observer`](#unregister_observer)
        - [`notify_observers`](#notify_observers)
2. [Clase Observer](#clase-observer)
    - [Descripción](#descripción-1)
    - [Métodos](#métodos-1)
        - [`update`](#update)
3. [Clases de Evento](#clases-de-evento)
    - [Descripción](#descripción-2)
    - [Eventos Concretos](#eventos-concretos)
4. [Observadores Concretos](#observadores-concretos)
    - [EmailNotifier](#emailnotifier)
    - [LogObserver](#logobserver)
    - [CustomObserver](#customobserver)
5. [Ejemplos de Uso](#ejemplos-de-uso)
    - [Ejemplo Básico](#ejemplo-básico)
    - [Ejemplo Asíncrono](#ejemplo-asíncrono)
6. [Buenas Prácticas](#buenas-prácticas)
7. [Recursos Adicionales](#recursos-adicionales)

---

## Clase Subject

### Descripción

La clase `Subject` es el núcleo del **Patrón Observer** en **ObserverKit**. Se encarga de manejar la **suscripción** y **desregistro** de observadores, así como de **notificar** a todos los observadores registrados cuando ocurre un evento. Soporta tanto operaciones **síncronas** como **asíncronas**, lo que la hace versátil para diferentes contextos de uso.

### Métodos

#### `register_observer`

```python
async def register_observer(self, observer: Observer) -> None:
    """
    Registra un nuevo Observer.

    Args:
        observer (Observer): Instancia de una clase que hereda de Observer.
    """
    async with self._lock:
        if observer not in self._observers:
            self._observers.append(observer)
```

**Descripción:**  
Este método permite registrar un nuevo observador. Solo se aceptan instancias de clases que heredan de `Observer`. Si el observador ya está registrado, no se añade de nuevo para evitar duplicados.

**Parámetros:**
- `observer (Observer)`: Instancia de una clase que hereda de `Observer`.

#### `unregister_observer`

```python
async def unregister_observer(self, observer: Observer) -> None:
    """
    Desregistra un Observer existente.

    Args:
        observer (Observer): Instancia de una clase que hereda de Observer.
    """
    async with self._lock:
        if observer in self._observers:
            self._observers.remove(observer)
```

**Descripción:**  
Este método elimina un observador previamente registrado de la lista de observadores. Si el observador no está registrado, el método no realiza ninguna acción.

**Parámetros:**
- `observer (Observer)`: Instancia de una clase que hereda de `Observer`.

#### `notify_observers`

```python
async def notify_observers(self, event: Evento) -> None:
    """
    Notifica a todos los Observers registrados sobre un evento de manera asíncrona.

    Args:
        event (Evento): Instancia de una clase que hereda de Evento.
    """
    async with self._lock:
        observers_snapshot = list(self._observers)
    tasks = []
    for observer in observers_snapshot:
        task = asyncio.create_task(self._safe_notify(observer, event))
        tasks.append(task)
    # Espera a que todas las tareas terminen, manejando excepciones individualmente
    await asyncio.gather(*tasks, return_exceptions=True)
```

**Descripción:**  
Este método notifica a todos los observadores registrados sobre un evento específico. Crea tareas asíncronas para cada observador, permitiendo que las notificaciones se realicen de manera concurrente.

**Parámetros:**
- `event (Evento)`: Instancia de una clase que hereda de `Evento`.

#### `_safe_notify`

```python
async def _safe_notify(self, observer: Observer, event: Evento) -> None:
    """
    Notifica a un Observer y maneja excepciones de manera segura.

    Args:
        observer (Observer): Observador a notificar.
        event (Evento): Evento a notificar.
    """
    try:
        await observer.update(event)
    except Exception as e:
        # Loggear el error o manejarlo según sea necesario
        print(f"Error al notificar al observer {observer}: {e}")
        # Opcionalmente, puedes registrar el error en un sistema de logging
        raise NotificationError(f"Error al notificar al observer: {e}") from e
```

**Descripción:**  
Método interno que maneja la notificación a un observador específico y gestiona posibles excepciones que puedan ocurrir durante la actualización.

**Parámetros:**
- `observer (Observer)`: Observador a notificar.
- `event (Evento)`: Evento a notificar.

---

## Clase Observer

### Descripción

La clase abstracta `Observer` define la interfaz que deben implementar todos los observadores concretos. Utiliza **tipado genérico** para especificar el tipo de evento que maneja, garantizando así un manejo consistente y seguro de los eventos.

### Métodos

#### `update`

```python
async def update(self, event: T) -> None:
    """
    Método que será llamado cuando se notifique un evento.

    Args:
        event (T): Evento que ha sido notificado, donde T es una subclase de Evento.
    """
    pass
```

**Descripción:**  
Método abstracto que debe ser implementado por todas las clases que heredan de `Observer`. Este método es llamado cuando se notifica un evento.

**Parámetros:**
- `event (T)`: Evento que ha sido notificado, donde `T` es una subclase de `Evento`.

---

## Clases de Evento

### Descripción

Las clases de evento representan los diferentes tipos de eventos que pueden ocurrir en tu aplicación. Cada evento debe heredar de la clase abstracta `Evento` y definir sus propios atributos y validaciones.

### Eventos Concretos

- **`NuevoUsuarioEvento`**

  Evento que se emite cuando se crea un nuevo usuario.

  **Atributos:**
  - `tipo: str` - Siempre tiene el valor `"nuevo_usuario"`.
  - `datos: dict` - Contiene información relevante del usuario, como `email` y `mensaje`.

- **`CompraRealizadaEvento`**

  Evento que se emite cuando se realiza una compra.

  **Atributos:**
  - `tipo: str` - Siempre tiene el valor `"compra_realizada"`.
  - `datos: dict` - Contiene información de la compra, como `usuario` y `monto`.

- **`ActualizacionSistemaEvento`**

  Evento que se emite para actualizaciones del sistema o acciones de destrucción.

  **Atributos:**
  - `tipo: str` - Puede ser `"actualizacion_sistema"` o `"destruir"`.
  - `datos: dict` - Contiene detalles de la actualización o la razón para destruir.

**Ejemplo de Definición de Eventos Concretos:**

```python
from dataclasses import dataclass, field
from typing import Any, Dict
from .evento import Evento

@dataclass(frozen=True)
class NuevoUsuarioEvento(Evento):
    tipo: str = field(init=False, default="nuevo_usuario")
    datos: Dict[str, Any]

    def __post_init__(self):
        if 'email' not in self.datos or 'mensaje' not in self.datos:
            raise ValueError("Datos incompletos para NuevoUsuarioEvento: 'email' y 'mensaje' son requeridos.")

@dataclass(frozen=True)
class CompraRealizadaEvento(Evento):
    tipo: str = field(init=False, default="compra_realizada")
    datos: Dict[str, Any]

    def __post_init__(self):
        if 'usuario' not in self.datos or 'monto' not in self.datos:
            raise ValueError("Datos incompletos para CompraRealizadaEvento: 'usuario' y 'monto' son requeridos.")

@dataclass(frozen=True)
class ActualizacionSistemaEvento(Evento):
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
```

---

## Observadores Concretos

### EmailNotifier

```python
from .observer import Observer
from .eventos_concretos import NuevoUsuarioEvento
import asyncio

class EmailNotifier(Observer[NuevoUsuarioEvento]):
    async def update(self, event: NuevoUsuarioEvento) -> None:
        await self.enviar_email(event.datos)

    async def enviar_email(self, datos: dict) -> None:
        # Simulación de envío de email asíncrono
        await asyncio.sleep(1)  # Simula tiempo de envío
        print(f"Enviando email a {datos['email']} sobre {datos['mensaje']}")
```

**Descripción:**  
`EmailNotifier` es un observador concreto que maneja el evento `NuevoUsuarioEvento`. Cuando se recibe este evento, simula el envío de un correo electrónico al nuevo usuario.

### LogObserver

```python
from .observer import Observer
from .events import Evento
import asyncio

class LogObserver(Observer[Evento]):
    async def update(self, event: Evento) -> None:
        await self.log_event(event)

    async def log_event(self, event: Evento) -> None:
        # Simulación de logging asíncrono
        await asyncio.sleep(0.5)  # Simula tiempo de logging
        print(f"Registrando evento: {event.tipo} con datos {event.datos}")
```

**Descripción:**  
`LogObserver` es un observador concreto que maneja cualquier instancia de `Evento`. Al recibir un evento, simula el registro de dicho evento.

### CustomObserver

```python
from .observer import Observer
from .eventos_concretos import ActualizacionSistemaEvento
from .subject import Subject

class CustomObserver(Observer[ActualizacionSistemaEvento]):
    def __init__(self, name: str, subject: Subject):
        self.name = name
        self.subject = subject

    async def update(self, event: ActualizacionSistemaEvento) -> None:
        print(f"{self.name}: Evento {event.tipo} recibido con datos {event.datos}")
        # Condición para desregistrarse
        if event.tipo == "destruir":
            await self.subject.unregister_observer(self)
            print(f"{self.name}: Desregistrado después de recibir el evento 'destruir'.")
```

**Descripción:**  
`CustomObserver` es un observador concreto que maneja el evento `ActualizacionSistemaEvento`. Al recibir un evento de tipo `"destruir"`, se desregistra a sí mismo del `Subject`.

---

## Ejemplos de Uso

### Ejemplo Básico

Este ejemplo muestra cómo utilizar **ObserverKit** de manera básica, registrando observadores y notificando eventos.

```python
import asyncio
from observerkit.subject import Subject
from observerkit.concrete_observers import EmailNotifier, LogObserver
from observerkit.events import NuevoUsuarioEvento, CompraRealizadaEvento

async def main():
    # Crear el Subject
    subject = Subject()

    # Crear Observers
    email_notifier = EmailNotifier()
    log_observer = LogObserver()

    # Registrar Observers
    await subject.register_observer(email_notifier)
    await subject.register_observer(log_observer)

    # Crear y notificar eventos
    evento1 = NuevoUsuarioEvento(datos={"email": "usuario@example.com", "mensaje": "Bienvenido a la plataforma!"})
    evento2 = CompraRealizadaEvento(datos={"usuario": "usuario@example.com", "monto": 150.0})

    await subject.notify_observers(evento1)
    await subject.notify_observers(evento2)

    # Desregistrar un Observador
    await subject.unregister_observer(email_notifier)

    # Notificar otro evento (solo LogObserver recibirá)
    evento3 = CompraRealizadaEvento(datos={"usuario": "usuario@example.com", "monto": 200.0})
    await subject.notify_observers(evento3)

if __name__ == "__main__":
    asyncio.run(main())
```

**Salida Esperada:**

```
Enviando email a usuario@example.com sobre Bienvenido a la plataforma!
Registrando evento: nuevo_usuario con datos {'email': 'usuario@example.com', 'mensaje': 'Bienvenido a la plataforma!'}
Enviando email a usuario@example.com sobre Bienvenido a la plataforma!
Registrando evento: compra_realizada con datos {'usuario': 'usuario@example.com', 'monto': 150.0'}
Registrando evento: compra_realizada con datos {'usuario': 'usuario@example.com', 'monto': 200.0'}
```

### Ejemplo Asíncrono

Este ejemplo muestra cómo manejar eventos de manera asíncrona utilizando **ObserverKit**.

```python
import asyncio
from observerkit.subject import Subject
from observerkit.concrete_observers import EmailNotifier, LogObserver, CustomObserver
from observerkit.events import NuevoUsuarioEvento, CompraRealizadaEvento, ActualizacionSistemaEvento

async def main():
    # Crear el Subject
    subject = Subject()

    # Crear Observers
    email_notifier = EmailNotifier()
    log_observer = LogObserver()
    custom_observer = CustomObserver(name="CustomObserver1", subject=subject)

    # Registrar Observers
    await subject.register_observer(email_notifier)
    await subject.register_observer(log_observer)
    await subject.register_observer(custom_observer)

    # Crear y notificar eventos
    evento1 = NuevoUsuarioEvento(datos={"email": "usuario1@example.com", "mensaje": "Bienvenido a la plataforma!"})
    evento2 = CompraRealizadaEvento(datos={"usuario": "usuario1@example.com", "monto": 150.0})
    evento3 = ActualizacionSistemaEvento(tipo="destruir", datos={"razon": "Cierre de aplicación"})

    await subject.notify_observers(evento1)
    await subject.notify_observers(evento2)
    await subject.notify_observers(evento3)

    # Notificar otro evento (custom_observer ya no recibirá)
    evento4 = CompraRealizadaEvento(datos={"usuario": "usuario1@example.com", "monto": 200.0})
    await subject.notify_observers(evento4)

if __name__ == "__main__":
    asyncio.run(main())
```

**Salida Esperada:**

```
Enviando email a usuario1@example.com sobre Bienvenido a la plataforma!
Registrando evento: nuevo_usuario con datos {'email': 'usuario1@example.com', 'mensaje': 'Bienvenido a la plataforma!'}
CustomObserver1: Evento nuevo_usuario recibido con datos {'email': 'usuario1@example.com', 'mensaje': 'Bienvenido a la plataforma!'}
Enviando email a usuario1@example.com sobre Bienvenido a la plataforma!
Registrando evento: compra_realizada con datos {'usuario': 'usuario1@example.com', 'monto': 150.0'}
CustomObserver1: Evento compra_realizada recibido con datos {'usuario': 'usuario1@example.com', 'monto': 150.0'}
Registrando evento: destruir con datos {'razon': 'Cierre de aplicación'}
CustomObserver1: Evento destruir recibido con datos {'razon': 'Cierre de aplicación'}
CustomObserver1: Desregistrado después de recibir el evento 'destruir'.
Registrando evento: compra_realizada con datos {'usuario': 'usuario1@example.com', 'monto': 200.0'}
```

---

