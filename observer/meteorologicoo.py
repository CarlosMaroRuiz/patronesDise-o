""" 
Crea un sistema de alertas meteorologicas donde varias ciudades 
están suscritas a un servicio meteorológico. 
Cada vez que se actualiza el clima, las ciudades
suscritas reciben una alerta con la nueva información.
"""

import time #Esto es inrelevante este ser usa para simular un tiempo de espera
class ServicioMeteorologico:#Este sera el observable que notificara
    def __init__(self):
        self.ciudades = []
    
    def agregarCiudad(self,ciudad):
        self.ciudades.append(ciudad)
    
    def eliminarCiudad(self,ciudad):
        self.ciudades.remove(ciudad)
        
            
    
    def notificar(self,mensaje):
        for ciudad in self.ciudades:
            ciudad.update(mensaje)


class Ciudad:#Este sera el obserber que recibira los mensaje
    def __init__(self,name):
        self.name = name
    def update(self,mensaje):
        print(f"{self.name} recibio la alerta de: {mensaje}")
        

if __name__ == "__main__":
    noticias = ["Lluvia intensa", "Tormenta eléctrica", "Viento fuerte"]
    servicio = ServicioMeteorologico()
    ciudad1 = Ciudad("Chicago")
    ciudad2 = Ciudad("San Francisco")
    
    #Agregaremos nuestros observers al observable
    servicio.agregarCiudad(ciudad1)
    servicio.agregarCiudad(ciudad2)
    
    
    for noticia in noticias:
        time.sleep(2)
        servicio.notificar(noticia)        
