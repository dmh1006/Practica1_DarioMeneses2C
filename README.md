# Práctica 1 – Pac-Man Simplificado  
**Asignatura:** Sistemas Inteligentes  
**Grado:** Ingeniería de la Salud  
**Universidad:** Universidad de Burgos


## Descripción

Esta práctica consiste en el desarrollo de una versión simplificada del juego Pac-Man, cuyo objetivo es aplicar de forma práctica los contenidos vistos en la asignatura de Sistemas Inteligentes.

A lo largo del trabajo se implementa la lógica básica del juego, incluyendo el movimiento del personaje, la interacción con el tablero y la gestión de la comida y la puntuación. Para ello, se ha puesto especial énfasis en organizar correctamente el código y separar la lógica del sistema de la forma en la que se muestra al usuario.

El proyecto permite ejecutar el juego de dos maneras distintas: mediante un entorno visual interactivo basado en un notebook y a través de la consola, reutilizando en ambos casos la misma base lógica del juego.


## Descripción de archivos

- **Practica1.ipynb**: Notebook principal de la práctica. Contiene el modo visual del juego mediante HTML y botones, utilizando el código base proporcionado por el profesor.
- **Practica1_Rubrica.ipynb**: Rúbrica de evaluación y plantilla oficial de la práctica.
- **pacman.py**: Archivo ejecutable que permite jugar al Pac-Man en modo consola.
- **proyecto_pacman/utils.py**: Funciones auxiliares del juego (movimientos, tableros, menú y control por teclado).
- **proyecto_pacman/clases.py**: Implementación de la clase `JuegoPacman`, que contiene la lógica principal del juego.
- **spritesPacman/**: Carpeta con los recursos gráficos utilizados en el modo visual (material docente).

## Funcionamiento del juego

El juego se puede ejecutar en dos modos distintos: modo visual y modo consola.

### Modo visual (Notebook)

El modo visual se ejecuta desde el archivo `Practica1.ipynb`.

Características:
- Control mediante botones de dirección.
- Representación gráfica del tablero usando HTML e imágenes.
- Actualización automática del estado del juego tras cada movimiento.
- Finalización de la partida cuando se consume toda la comida.

Este modo utiliza directamente el código proporcionado por el profesor como parte del enunciado de la práctica.

### Modo consola

El modo consola permite ejecutar el juego desde la terminal del sistema, ofreciendo una alternativa sin interfaz gráfica. 
Para iniciar el juego es necesario situarse en la raíz del proyecto y ejecutar el archivo `pacman.py` mediante el comando `python pacman.py`. 

El control del Pac-Man se realiza utilizando las flechas del teclado, mientras que la tecla `ESC` permite finalizar la ejecución en cualquier momento. Tras cada movimiento, el estado actual del tablero se muestra en formato texto junto con la puntuación acumulada, actualizándose progresivamente hasta que se consume toda la comida disponible o se interrumpe la partida.


## Lógica del juego

- El tablero se representa como una matriz de valores:
  - `1` indica una pared.
  - `0` indica un camino transitable.
- La comida se inicializa en todas las casillas libres del tablero.
- El Pac-Man solo puede desplazarse a casillas libres.
- Cada comida consumida incrementa la puntuación en una unidad.
- El juego termina cuando no queda comida disponible.

## Requisitos y dependencias

### Requisitos
- Python 3.10 o superior.

### Dependencias
Las dependencias necesarias para ejecutar el proyecto se encuentran en el archivo `requirements.txt`:

pynput
ipywidgets
IPython

Se recomienda la utilización de un entorno virtual para la instalación de dichas dependencias.

## Autor

**Darío Meneses**  
Grado en Ingeniería de la Salud  
Universidad de Burgos
