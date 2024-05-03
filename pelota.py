import pygame
import random
from constants import ALTO_ESCENARIO, ANCHO_ESCENARIO, COLOR_PELOTA, MARGEN_ESCENARIO

class Pilota:
    VELOCITAT = 5
    MIDA = 10

    def __init__(self):
        self.color = COLOR_PELOTA
        self.posX = ANCHO_ESCENARIO // 2 - self.MIDA // 2
        self.posY = ALTO_ESCENARIO // 2 - self.MIDA // 2
        self.velX = self.VELOCITAT * random.choice([-1, 1])
        self.velY = self.VELOCITAT * random.choice([-1, 1])

    def dibuixa_pilota(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.posX, self.posY, self.MIDA, self.MIDA))

    def actualitza(self):
        self.posX += self.velX
        self.posY += self.velY

        if self.posY <= 0 or self.posY >= (ALTO_ESCENARIO - MARGEN_ESCENARIO) - self.MIDA:
            self.velY = -self.velY

    def reinicia(self):
        self.posX = ANCHO_ESCENARIO // 2 - self.MIDA // 2
        self.posY = ALTO_ESCENARIO // 2 - self.MIDA // 2
        self.velX = self.VELOCITAT * random.choice([-1, 1])
        self.velY = self.VELOCITAT * random.choice([-1, 1])
