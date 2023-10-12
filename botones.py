from var import *
import pygame
from clasespy import objetopy
import os
dir = "sprites/"

class Boton_palay(objetopy):
    def __init__(self, ancho_p, alto_p,  x, y):
        super().__init__(x, y)

        imagen_path = os.path.join(dir, "botonplay.png")  # Unir el directorio con el nombre del archivo
        self.image = pygame.image.load(imagen_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (ancho_p, alto_p))
        self.initrect()