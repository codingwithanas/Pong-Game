import pygame
from constants import JUGADOR_ANCHO, JUGADOR_ALTO, ALTO_ESCENARIO, MARGEN_ESCENARIO

class Jugador:
    def __init__(self, posX, posY, color, velocidad):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.ancho = JUGADOR_ANCHO
        self.alto = JUGADOR_ALTO
        self.velocidad = velocidad  

    def dibuja_jugador(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.posX, self.posY, self.ancho, self.alto))

    def mover(self, arriba, abajo):
        teclas = pygame.key.get_pressed()
        if teclas[arriba] and self.posY - self.velocidad >= MARGEN_ESCENARIO:
            self.posY -= self.velocidad
        if teclas[abajo] and self.posY + self.alto + self.velocidad <= ALTO_ESCENARIO - MARGEN_ESCENARIO:
            self.posY += self.velocidad