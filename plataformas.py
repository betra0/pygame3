from constantes import *
import pygame
from clasespy import objetopy

class Plataforma(objetopy):
    def __init__(self, ancho_plataforma, x, ytop):
        y = ((ALTO -ytop))//2+ytop
        super().__init__(x, y)
        self.image = pygame.Surface((ancho_plataforma, ((ALTO -ytop))))
        self.image.fill((80, 80, 120))
        self.initrect()
        self.info = "nonexd"



    def update(self):
        self.velpos(-4, 0)
        self.eliminarplataforma()

    def eliminarplataforma(self):
        self.killxlimit()
        if self.iskill:
            self.kill()
