import pygame
import sys
from constants import *
from jugador import Jugador

def main():
    pygame.init()
    finestraJoc = pygame.display.set_mode((ANCHO_ESCENARIO, ALTO_ESCENARIO))
    rellotge = pygame.time.Clock()
    gameOver = False

    jugador1 = Jugador(MARGEN_ESCENARIO, ALTO_ESCENARIO // 2 - JUGADOR_ALTO // 2, COLOR_JUGADOR1)
    jugador2 = Jugador(ANCHO_ESCENARIO - MARGEN_ESCENARIO - JUGADOR_ANCHO, ALTO_ESCENARIO // 2 - JUGADOR_ALTO // 2, COLOR_JUGADOR2)

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        finestraJoc.fill(COLOR_FONDO)
        pygame.draw.rect(finestraJoc, VERD, (MARGEN_ESCENARIO, MARGEN_ESCENARIO, ANCHO_ESCENARIO - 2 * MARGEN_ESCENARIO, ALTO_ESCENARIO - 2 * MARGEN_ESCENARIO))

        jugador1.dibuja_jugador(finestraJoc)
        jugador2.dibuja_jugador(finestraJoc)

        pygame.display.update()
        rellotge.tick(30)

if __name__ == "__main__":
    main()
# 