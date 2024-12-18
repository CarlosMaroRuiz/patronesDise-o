from observer_repository.observer_kit.subject import Subject
from observer_repository.observer_kit_implementation import NuevoUsuarioEvento, CompraRealizadaEvento
from observer_repository.observer_kit_implementation.observers_concrete import EmailNotifier, LogObserver


async def main():

    subject = Subject()
    email_notifier = EmailNotifier()
    log_observer = LogObserver()

    await subject.register_observer(email_notifier)
    await subject.register_observer(log_observer)
    evento1 = NuevoUsuarioEvento(datos={"email": "usuario@example.com", "mensaje": "Bienvenido a la plataforma!"})
    evento2 = CompraRealizadaEvento(datos={"usuario": "usuario@example.com", "monto": 150.0})

    await subject.notify_observers(evento1)
    await subject.notify_observers(evento2)

    await subject.unregister_observer(email_notifier)

    evento3 = CompraRealizadaEvento(datos={"usuario": "usuario@example.com", "monto": 200.0})
    await subject.notify_observers(evento3)


