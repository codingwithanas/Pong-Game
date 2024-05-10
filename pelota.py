import pygame
import random
from constants import ANCHO_ESCENARIO, ALTO_ESCENARIO, MARGEN_ESCENARIO, COLOR_PELOTA

class ObjecteEscenari:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color

    def Pinta(self, pantalla):
        pass 

class Pilota(ObjecteEscenari):
    VELOCITAT = 5
    MIDA = 10

    def __init__(self):
        super().__init__(ANCHO_ESCENARIO // 2 - self.MIDA // 2, ALTO_ESCENARIO // 2 - self.MIDA // 2, COLOR_PELOTA)
        self.velX = self.VELOCITAT * random.choice([-1, 1])
        self.velY = self.VELOCITAT * random.choice([-1, 1])

    def Pinta(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.posX, self.posY, self.MIDA, self.MIDA))

    def MourePilota(self):
        self.posX += self.velX
        self.posY += self.velY

        if self.posY <= MARGEN_ESCENARIO or self.posY >= ALTO_ESCENARIO - MARGEN_ESCENARIO - self.MIDA:
            self.velY = -self.velY

    def ReiniciaPilota(self):
        self.posX = ANCHO_ESCENARIO // 2 - self.MIDA // 2
        self.posY = ALTO_ESCENARIO // 2 - self.MIDA // 2
        self.velX = self.VELOCITAT * random.choice([-1, 1])
        self.velY = self.VELOCITAT * random.choice([-1, 1])
