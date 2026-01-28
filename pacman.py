"""
pacman.py

Ejecución por consola del Pac-Man simplificado.
Se controla con las flechas del teclado y se sale con ESC.
"""

import os
import time

from proyecto_pacman.utils import tableros, mostrar_menu, leer_teclado
from proyecto_pacman.clases import JuegoPacman


def limpiar_consola():
    """Limpia la consola para que el tablero se vaya actualizando."""
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    # Elegimos tablero con el menú
    dificultad = mostrar_menu()
    tablero = tableros[dificultad]

    # Posición inicial como en el ejemplo del profesor
    juegoPacman = JuegoPacman(tablero, [1, 1])

    # Bucle principal leyendo teclas
    for mov, terminado in leer_teclado():
        if terminado:
            break

        # Solo actualizamos si hay una pulsación válida
        if mov is not None:
            juegoPacman.actualizaJuego(mov)

        # Mostrar por consola
        limpiar_consola()
        print(str(juegoPacman))
        print("\nPuntos:", juegoPacman.get_puntos())
        print("Flechas para mover | ESC para salir")

        # Si se termina la comida, acaba
        if juegoPacman.comida_agotada():
            print("\nEl juego ha terminado. Has ganado con", juegoPacman.get_puntos(), "puntos")
            break

        time.sleep(0.05)
