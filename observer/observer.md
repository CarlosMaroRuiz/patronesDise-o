<div align="center">
  <img src="https://via.placeholder.com/468x60/000000/00FF00?text=Observable" />
</div>
<br/>
<br/>
<h2 align="center">Definicion rapida</h2>
<p align="center">
  El patrón <strong>Observer</strong> es un mecanismo en el que un objeto (<em>Observable</em>) notifica automáticamente a otros objetos 
  (<em>Observers</em>) cuando ocurre un cambio en su estado. Esto permite que los objetos dependientes se actualicen 
  sin estar directamente conectados entre sí, haciendo el sistema más flexible y desacoplado.
</p>

<br/>

<h3 align="center">Ejemplo básico</h3>

<div align="center">
  <a href="https://github.com/CarlosMaroRuiz/patronesDise-o/edit/main/observer/Ejemplo.py" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Ver%20Ejemplo-Ejemplo%20Observer-green?style=for-the-badge" alt="Ejemplo de Observer" />
  </a>
</div>

<div align="center">
  <a href="https://github.com/CarlosMaroRuiz/patronesDise-o/edit/main/observer/noticias.py" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Ver%20Ejemplo-Ejemplo%20Noticias%20Observer-green?style=for-the-badge" alt="Ejemplo noticias de observer" />
  </a>
</div>

<br/>
<br/>
<h2 align="center">Ejercicios</h2>

<h2 align="center">Ejercicios</h2>

<h3>Lista de Ejercicios</h3>

<ol>
  <li>
    <strong>Ejercicio 1:</strong>Crea un codigo de alertas meteorologicas donde varias ciudades 
están suscritas a un servicio meteorológico. 
Cada vez que se actualiza el clima, las ciudades
suscritas reciben una alerta con la nueva información..
    <br/>
    <p> <strong>Posible Solucion:</strong></p>
    <a href="https://github.com/CarlosMaroRuiz/patronesDise-o/blob/main/observer/meteorologicoo.py" style="text-decoration: none;">
      <img src="https://img.shields.io/badge/Ver%20Ejercicio-Ejercicio%201-blue?style=for-the-badge" alt="Ver Ejercicio 1" />
    </a>

  </li>
    <br/>
<li>
  <strong>Ejercicio 2:</strong> Crea un sistema de monitoreo de temperatura donde varios sensores 
estan suscritos a un sistema central. 
Cada vez que uno de los sensores detecta un cambio significativo en la temperatura, 
el sistema central recibe una alerta con la nueva información. 
El monitoreo de los sensores se realiza de manera concurrente utilizando hilos,
y el sistema detiene la monitorización automáticamente después de 10 segundos.
 <p> <strong>Posible Solucion:</strong></p>
    <a href="https://github.com/CarlosMaroRuiz/patronesDise-o/blob/main/observer/sensore.py" style="text-decoration: none;">
      <img src="https://img.shields.io/badge/Ver%20Ejercicio-Ejercicio%202-blue?style=for-the-badge" alt="Ver Ejercicio 1" />
    </a>
  
</li>

</ol>
