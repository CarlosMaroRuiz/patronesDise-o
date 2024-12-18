class Observable:
    def __init__(self):
        self._observers = []  # Lista para almacenar los observers
    
    def register(self, observer):  # metodo para agregar observer a la lista
       
        self._observers.append(observer)
    
    def unregister(self, observer):    # Elimina un observer de la lista
     
        self._observers.remove(observer)
    
    def notify_observers(self):  # Notifica a todos los observers llamando al método update()
        for observer in self._observers:
            observer.update(self)
    
    def some_business_logic(self):
        print("El estado ha cambiado en el Subject.")
        self.notify_observers()


class Observer:#sera nuestra  clase abstracta para asi firma un contrarto
    def update(self, subject):
        pass

#creacion de observadores
class ConcreteObserverA(Observer):
    def update(self, observable):
        print("ConcreteObserverA ha sido notificado.")


class ConcreteObserverB(Observer):
    def update(self, subject):
        print("ConcreteObserverB ha sido notificado.")


# Uso del patrón Observer
if __name__ == "__main__":
    subject = Observable()
    
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()
    
    
    #registrarenmos a nuestros observadores
    subject.register(observer_a)
    subject.register(observer_b) 
    
    subject.some_business_logic()
    
