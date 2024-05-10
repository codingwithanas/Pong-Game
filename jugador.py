import pygame
from constants import JUGADOR_ALTO, JUGADOR_ANCHO, MARGEN_ESCENARIO, ALTO_ESCENARIO

class ObjecteEscenari:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color

    def Pinta(self, pantalla):
        pass
    
class Jugador:
    def __init__(self, posX, posY, color, velocidad):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.ancho = JUGADOR_ANCHO
        self.alto = JUGADOR_ALTO
        self.velocidad = velocidad
        self.punts = 0 

    def Pinta(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.posX, self.posY, self.ancho, self.alto))

    def MoureAmunt(self):
        if self.posY - self.velocidad >= MARGEN_ESCENARIO:
            self.posY -= self.velocidad

    def MoureAvall(self):
        if self.posY + self.alto + self.velocidad <= ALTO_ESCENARIO - MARGEN_ESCENARIO:
            self.posY += self.velocidad
