import pygame
from constants import JUGADOR_ANCHO, JUGADOR_ALTO

class Jugador:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.ancho = JUGADOR_ANCHO
        self.alto = JUGADOR_ALTO

    def dibuja_jugador(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.posX, self.posY, self.ancho, self.alto))
