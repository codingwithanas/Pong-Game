import pygame
import sys
import random
from constants import *
from jugador import Jugador
from pelota import Pilota

def main():
    pygame.init()
    finestraJoc = pygame.display.set_mode((ANCHO_ESCENARIO, ALTO_ESCENARIO))
    rellotge = pygame.time.Clock()
    gameOver = False

    jugador1 = Jugador(MARGEN_ESCENARIO, ALTO_ESCENARIO // 2 - JUGADOR_ALTO // 2, COLOR_JUGADOR1, VELOCIDAD_JUGADOR)
    jugador2 = Jugador(ANCHO_ESCENARIO - MARGEN_ESCENARIO - JUGADOR_ANCHO, ALTO_ESCENARIO // 2 - JUGADOR_ALTO // 2, COLOR_JUGADOR2, VELOCIDAD_JUGADOR)
    pilota = Pilota()  #

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        jugador1.mover(pygame.K_w, pygame.K_s)
        jugador2.mover(pygame.K_UP, pygame.K_DOWN)

        pilota.actualitza()

        if pilota.posY <= MARGEN_ESCENARIO or pilota.posY >= ALTO_ESCENARIO - MARGEN_ESCENARIO:
            pilota.velY = -pilota.velY
        
        if pilota.posX <= jugador1.posX + JUGADOR_ANCHO and pilota.posY >= jugador1.posY and pilota.posY <= jugador1.posY + JUGADOR_ALTO:
            pilota.velX = -pilota.velX
            
        if pilota.posX >= jugador2.posX - JUGADOR_ANCHO // 2 and pilota.posY >= jugador2.posY and pilota.posY <= jugador2.posY + JUGADOR_ALTO:
            pilota.velX = -pilota.velX
        
        if pilota.posX <= 0 or pilota.posX >= ANCHO_ESCENARIO:
            pilota.reinicia()

        finestraJoc.fill(COLOR_FONDO)
        pygame.draw.rect(finestraJoc, VERD, (0, MARGEN_ESCENARIO, ANCHO_ESCENARIO - 2 * 0, ALTO_ESCENARIO - 2 * MARGEN_ESCENARIO))

        jugador1.dibuja_jugador(finestraJoc)
        jugador2.dibuja_jugador(finestraJoc)
        pilota.dibuixa_pilota(finestraJoc)

        pygame.display.update()
        rellotge.tick(30)

if __name__ == "__main__":
    main()
