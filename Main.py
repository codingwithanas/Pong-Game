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
    pilota = Pilota()

    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            jugador1.MoureAmunt()
        if keys[pygame.K_s]:
            jugador1.MoureAvall()
        if keys[pygame.K_UP]:
            jugador2.MoureAmunt()
        if keys[pygame.K_DOWN]:
            jugador2.MoureAvall()

        pilota.MourePilota()

        if pilota.posX <= jugador1.posX + jugador1.ancho and pilota.posY >= jugador1.posY and pilota.posY <= jugador1.posY + jugador1.alto:
            pilota.velX = -pilota.velX
        
        if pilota.posX >= jugador2.posX - jugador2.ancho and pilota.posY >= jugador2.posY and pilota.posY <= jugador2.posY + jugador2.alto:
            pilota.velX = -pilota.velX
        
        elif pilota.posX <= jugador1.posX or pilota.posX >= jugador2.posX:
            pilota.ReiniciaPilota()

        finestraJoc.fill(COLOR_FONDO)
        pygame.draw.rect(finestraJoc, VERD, (0, MARGEN_ESCENARIO, ANCHO_ESCENARIO - 2 * 0, ALTO_ESCENARIO - 2 * MARGEN_ESCENARIO))

        jugador1.Pinta(finestraJoc)
        jugador2.Pinta(finestraJoc)
        pilota.Pinta(finestraJoc)

        pygame.display.update()
        rellotge.tick(30)

if __name__ == "__main__":
    main()
