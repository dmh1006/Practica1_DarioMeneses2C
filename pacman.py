"""
pacman.py

Ejecución por consola del Pac-Man simplificado.
Control mediante flechas y salida con ESC.
"""

import time

from proyecto_pacman.utils import tableros, mostrar_menu, leer_teclado
from proyecto_pacman.clases import JuegoPacman


if __name__ == "__main__":
    dificultad = mostrar_menu()
    tablero = tableros[dificultad]

    juegoPacman = JuegoPacman(tablero, [1, 1])

    print("Flechas para mover | ESC para salir\n")
    print(str(juegoPacman))
    print("\nPuntos:", juegoPacman.get_puntos())

    for mov, terminado in leer_teclado():
        if terminado:
            break

        # Solo actualizamos si se ha pulsado una flecha
        if mov is None:
            time.sleep(0.03)
            continue

        juegoPacman.actualizaJuego(mov)

        # Sin limpiar consola: se imprime el nuevo estado debajo
        print("\n" + str(juegoPacman))
        print("\nPuntos:", juegoPacman.get_puntos())

        if juegoPacman.comida_agotada():
            print("\nEl juego ha terminado. Has ganado con",
                  juegoPacman.get_puntos(), "puntos")
            break
