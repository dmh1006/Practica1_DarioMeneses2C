"""
utils.py

Funciones y constantes auxiliares para la práctica.
Aquí se definen:
- movimientos (arriba, abajo, izquierda, derecha)
- tableros (diccionario con "easy", "medium", "hard")
- funciones básicas 
"""

from typing import List, Tuple, Dict

Tablero = List[List[int]]
Coordenada = List[int]            # [fila, columna]
Comida = List[Coordenada]

# Movimientos como (df, dc)
arriba: Tuple[int, int] = (-1, 0)
abajo: Tuple[int, int] = (1, 0)
izquierda: Tuple[int, int] = (0, -1)
derecha: Tuple[int, int] = (0, 1)

# Tableros como en la práctica
tableros: Dict[str, Tablero] = {
    "easy": [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ],
    "medium": [
        [1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,1,1,0,1,0,1],
        [1,0,1,0,1,1,0,1,0,1],
        [1,0,1,0,1,1,0,1,0,1],
        [1,0,0,0,1,1,0,0,0,1],
        [1,1,1,0,1,1,0,1,0,1],
        [1,1,1,0,0,0,0,1,1,1],
        [1,1,1,1,1,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1],
    ],
    "hard": [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
}


def posicion_esta_libre(tablero: Tablero, coordenada: Coordenada) -> bool:
    """
    Comprueba si la coordenada está dentro del tablero y si esa casilla es un 0.
    """
    f = coordenada[0]
    c = coordenada[1]

    if f < 0 or c < 0:
        return False
    if f >= len(tablero) or c >= len(tablero[0]):
        return False

    return tablero[f][c] == 0


def get_coordenadas_libres(tablero: Tablero) -> List[Coordenada]:
    """
    Devuelve una lista con todas las coordenadas libres (tablero == 0).
    """
    libres: List[Coordenada] = []
    for f in range(len(tablero)):
        for c in range(len(tablero[0])):
            if tablero[f][c] == 0:
                libres.append([f, c])
    return libres


def mueve(pacman: Coordenada, mov: Tuple[int, int]) -> Coordenada:
    """
    Devuelve la nueva coordenada tras aplicar el movimiento 'mov' a la coordenada 'pacman'.
    """
    return [pacman[0] + mov[0], pacman[1] + mov[1]]


def posicion_hay_comida(coordenada: Coordenada, comida: Comida) -> bool:
    """
    Devuelve True si la coordenada está en la lista de comida.
    """
    return coordenada in comida

def leer_teclado():
    """
    Lee el teclado con pynput y devuelve un generador.
    - Devuelve (mov, terminado)
    - mov es arriba/abajo/izquierda/derecha o None si no hay pulsación nueva
    - terminado es True si se pulsa ESC
    """
    from pynput import keyboard

    direccion = None
    terminado = False

    def on_press(tecla):
        nonlocal direccion, terminado

        if tecla == keyboard.Key.esc:
            terminado = True
            return False

        if tecla == keyboard.Key.up:
            direccion = arriba
        elif tecla == keyboard.Key.down:
            direccion = abajo
        elif tecla == keyboard.Key.left:
            direccion = izquierda
        elif tecla == keyboard.Key.right:
            direccion = derecha

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while True:
        if terminado:
            yield None, True
            break

        mov = direccion
        direccion = None
        yield mov, False

def mostrar_menu():
    """
    Muestra un menú sencillo por consola para seleccionar la dificultad.
    Devuelve la opción elegida como string: 'easy', 'medium' o 'hard'.
    """
    while True:
        print("=== PAC-MAN ===")
        print("Selecciona dificultad:")
        print("1 - Easy")
        print("2 - Medium")
        print("3 - Hard")

        opcion = input("Opción: ")

        if opcion == "1":
            return "easy"
        elif opcion == "2":
            return "medium"
        elif opcion == "3":
            return "hard"
        else:
            print("Opción no válida. Intenta de nuevo.\n")


