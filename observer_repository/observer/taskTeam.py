""" 
Crea un sistema de gestión de tareas donde varios miembros del equipo 
están suscritos a diferentes tareas de un proyecto. 
Cada vez que el estado de una tarea cambia, los miembros suscritos 
reciben una notificación con la nueva información. 
La asignación de miembros a las tareas se realiza de manera aleatoria, 
y cada vez que se actualiza el estado de una tarea, todos los miembros suscritos 
son notificados automaticamente sobre el cambio de estado.
"""
import random
import time
class Tarea:
    def __init__(self, name,status):
        self.name = name
        self.status = status
        self.miembros = []
    def agregarMiembros(self,miembro):
        self.miembros.append(miembro)
    def removerMiembros(self,miembros):
        self.miembros.remove(miembros)
    
    def actualizarEstatus(self,status):
        self.status = status
        self.notificarMiembros()
    def notificarMiembros(self):
        for miembro in self.miembros:
            miembro.actualizar(self.status,self.name)

class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre
    def actualizar(self,estatus,nombreTarea):
        print(f"Se ha actualizado la tarea {nombreTarea} a {estatus} para el miembro {self.nombre}")

tarea1 = Tarea("Desarollo de la api","pendiente")
tarea2 = Tarea("Desarollo de la frontend","pendiente")

miembros = ["jorge","Pepe","Carlos","juan","pedro"]

#logica para definir tareas de manera aleatoria
for miembro in miembros:
    if random.randint(0,1) == 0:
        tarea1.agregarMiembros(Miembro(miembro))
    else:
        tarea2.agregarMiembros(Miembro(miembro))
        
tarea1.actualizarEstatus("completada")
time.sleep(1)
tarea2.actualizarEstatus("revision")
time.sleep(2)
tarea2.actualizarEstatus("Completada")


