from var import *
import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a, K_SPACE)
from clasespy import objetopy

        
class Jugador(objetopy):
    def __init__(self):
        super()._init_()
        self.salto_presionado = False
        self.salto= False
        self.nosalto =True
        self.cantidad_salto = 1
        self.en_el_suelo = False  # Variable para rastrear si el jugador está en el suelo

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[K_w] or keys[K_SPACE]:
            self.salto_presionado = True
        else:
           self.salto_presionado = False


        if self.salto_presionado and not self.salto and self.nosalto:
            self.salto = True
            self.nosalto = False

        if not self.salto_presionado:
            self.nosalto = True

        print(self.salto)

        if self.salto and self.isonfloor(8):
            self.vely = -self.velocidad
        elif self.salto and not self.isonfloor(8) and self.cantidad_salto >= 1:
            self.vely = -self.velocidad
            self.cantidad_salto -=1
        elif not self.salto and self.isonfloor(8):
            self.cantidad_salto = 1


        self.simulargravedad()
        self.velpos(0, self.vely)
        self.simularparedes()

        self.salto = False












