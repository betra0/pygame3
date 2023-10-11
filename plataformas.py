from var import *
import pygame
from clasespy import objetopy

class Plataforma(objetopy):
    def __init__(self, ancho_plataforma, x, ytop):
        y = ((alto -ytop))//2+ytop
        super().__init__(x, y)
        self.image = pygame.Surface((ancho_plataforma, ((alto -ytop))))
        self.image.fill((100, 128, 255))
        self.initrect()
        self.info = "hola que hace dsajkl"



    def update(self):
        self.velpos(-4, 0)