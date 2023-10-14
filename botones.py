from var import *
import pygame
from clasespy import objetopy
import os
dir = "sprites/"

class Boton_palay(objetopy):
    def __init__(self,  x, y, tamaño):
        super().__init__(x, y)
        ancho_p = 4
        alto_p = 3
        ancho_p, alto_p = ancho_p* tamaño, alto_p* tamaño
        imagen_path = os.path.join(dir, "botonplay1.png")  # Unir el directorio con el nombre del archivo
        self.image = pygame.image.load(imagen_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (ancho_p, alto_p))
        self.initrect()

        self.botonpresionado = False

    def update(self):
        botones_presionados = pygame.mouse.get_pressed()  # Obtiene el estado de los botones del ratón

        if botones_presionados[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.botonpresionado = True
        else:
            self.botonpresionado = False
            
