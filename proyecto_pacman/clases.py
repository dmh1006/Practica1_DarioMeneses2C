"""
clases.py

Clase JuegoPacman.
Aquí se guarda el estado del juego (posición del pacman, comida, puntos)
y se implementan los métodos que pide la práctica para actualizar y mostrar el juego.
"""

from typing import List, Tuple

from proyecto_pacman.utils import (
    Tablero,
    Coordenada,
    Comida,
    posicion_esta_libre,
    get_coordenadas_libres,
    mueve,
    posicion_hay_comida,
)


class JuegoPacman:
    """
    Juego Pac-Man simplificado basado en una matriz:
    - 1 representa una pared
    - 0 representa un camino

    La representación en texto se usa tanto para consola como para HTML:
    - '#' pared
    - '@' pacman
    - '.' comida
    - ' ' hueco (camino sin comida)
    """

    def __init__(self, tablero: Tablero, pacman: Coordenada):
        """
        Inicializa el juego con un tablero y una posición inicial para el pacman.

        En cada partida se rellena el tablero con comida, es decir:
        - se coloca comida en todas las casillas libres (0)
        - excepto en la casilla donde empieza el pacman (si coincide, se "consume")
        """
        self.tablero: Tablero = tablero
        self.pacman: Coordenada = [pacman[0], pacman[1]]

        # La comida se inicializa en todas las coordenadas libres del tablero
        self.comida: Comida = get_coordenadas_libres(self.tablero)

        # Puntuación inicial
        self.puntos: int = 0

        # Si el pacman empieza sobre una comida, se considera comida consumida
        if posicion_hay_comida(self.pacman, self.comida):
            self.comida.remove(self.pacman)
            self.puntos += 1

    def get_puntos(self) -> int:
        """
        Devuelve la puntuación actual.
        Este método se usa en el visor HTML del profesor.
        """
        return self.puntos

    def comida_agotada(self) -> bool:
        """
        Indica si ya no queda comida en el tablero.
        Si no queda comida, el juego termina.
        """
        return len(self.comida) == 0

    def actualizaJuego(self, mov: Tuple[int, int]) -> None:
        """
        Actualiza el estado del juego a partir de un movimiento.

        Reglas:
        - Se calcula la nueva posición con mueve()
        - Solo se actualiza la posición si la casilla destino es libre
        - Si al moverse cae en una casilla con comida, se elimina y suma 1 punto
        """
        nueva_pos = mueve(self.pacman, mov)

        # Si la casilla destino no es libre (pared o fuera del tablero), no se mueve
        if not posicion_esta_libre(self.tablero, nueva_pos):
            return

        # Se actualiza la posición del pacman
        self.pacman = nueva_pos

        # Si hay comida en la nueva posición, se consume
        if posicion_hay_comida(self.pacman, self.comida):
            self.comida.remove(self.pacman)
            self.puntos += 1

    def juegoString(self) -> str:
        """
        Construye un string con el estado actual del tablero.

        Para cada casilla:
        - Si es pared (1) -> '#'
        - Si es pacman -> '@'
        - Si hay comida -> '.'
        - Si es camino vacío -> ' '
        """
        filas: List[str] = []

        for f in range(len(self.tablero)):
            linea = ""
            for c in range(len(self.tablero[0])):
                if self.tablero[f][c] == 1:
                    linea += "#"
                else:
                    if [f, c] == self.pacman:
                        linea += "@"
                    elif [f, c] in self.comida:
                        linea += "."
                    else:
                        linea += " "
            filas.append(linea)

        return "\n".join(filas)

    def __str__(self) -> str:
        """
        Permite usar str(juegoPacman). El código del profesor lo utiliza.
        """
        return self.juegoString()

    def __repr__(self) -> str:
        """
        Representación útil al inspeccionar el objeto en notebooks.
        """
        return self.juegoString()
