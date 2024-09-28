""" 
Crea un sistema de monitoreo de temperatura donde varios sensores 
estan suscritos a un sistema central. 
Cada vez que uno de los sensores detecta un cambio significativo en la temperatura, 
el sistema central recibe una alerta con la nueva información. 
El monitoreo de los sensores se realiza de manera concurrente utilizando hilos,
y el sistema detiene la monitorización automáticamente después de 10 segundos.

"""


import threading
import time
import random

terminatedMonitoring = False
class SensorTemperatura: #Sensor de Temperatura (Observable)
    def __init__(self, nombre):
        self.nombre = nombre
        self.observers = []
        self.temperatura_actual = random.uniform(15.0, 30.0)

    def registrar_observer(self, observer):
        self.observers.append(observer)

    def eliminar_observer(self, observer):
        self.observers.remove(observer)

    def notificar_observers(self):
        for observer in self.observers:
            observer.update(self.nombre, self.temperatura_actual)

    def monitorear_temperatura(self):
        global terminatedMonitoring
        while not terminatedMonitoring:
            nueva_temperatura = random.uniform(15.0, 30.0)
            if abs(nueva_temperatura - self.temperatura_actual) > 2.0:  
                self.temperatura_actual = nueva_temperatura
                self.notificar_observers()
            time.sleep(random.uniform(1, 3)) 


def terminateTheardings():#Esta funcion se hace para terminar en un cierto tiempo los hilos
    global terminatedMonitoring
    time.sleep(10)
    terminatedMonitoring = True
    
    
class SistemaCentral:#simulara ser el observador(OBSERVER)
    def update(self, nombre_sensor, temperatura):
        print(f"[Alerta] {nombre_sensor}: la temperatura ha cambiado a {temperatura:.2f}°C")


def gestionar_sensor(sensor):#funcion que permitira inicializar los el monitoreo de los sensores
    sensor.monitorear_temperatura()

if __name__ == "__main__":

    sistema_central = SistemaCentral()

    sensor1 = SensorTemperatura("dht11")
    sensor2 = SensorTemperatura("lm35")
    sensor3 = SensorTemperatura("dht22")

    #el sistema se central se suscribira a todos los sensores(OBSERVABLE)
    sensor1.registrar_observer(sistema_central)
    sensor2.registrar_observer(sistema_central)
    sensor3.registrar_observer(sistema_central)


    hilos = []
    #Se aplica un hilo para cada sensor para simular que se esten monitoreando
    for sensor in [sensor1, sensor2, sensor3]:
        hilo = threading.Thread(target=gestionar_sensor, args=(sensor,))
        hilos.append(hilo)
        hilo.start()
    
    #Se aplica un hilo para terminar en cierto tiempo los hilos
    hilo = threading.Thread(target=terminateTheardings)
    hilo.start()
    hilo.join()

    
    for hilo in hilos:
        hilo.join()
