from var import *
import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a, K_SPACE)
class objetopy(pygame.sprite.Sprite):
    def _init_(self):
        super().__init__()
        self.tamaño = tamaño_player
        self.image = pygame.Surface((self.tamaño, self.tamaño))
        self.image.fill((100, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (350, 000)
        self.posx, self.posy = self.rect.center
        self.velocidad = 18
        self.gravedad = 0.5
        self.velx = 0
        self.vely = 0

    def savepos(self, x=None, y= None):
        if x:
            self.posx = x
        if y:
            self.posy = y
        self.rect.center =round(self.posx), round(self.posy)
    def velpos(self, x=None, y=None):
        if x:
            self.posx += x
        if y:
            self.posy += y
        self.rect.center =round(self.posx), round(self.posy)

    def simularparedes(self):
        if self.posy+self.tamaño/2 > alto:
            self.posy = alto-self.tamaño/2
            self.savepos(y = self.posy)

    def simulargravedad(self):
        self.vely += self.gravedad
    def isonfloor(self, n = 0):
        retorno = False
        if self.posy+self.tamaño/2+n >= alto:
            retorno = True
        return retorno
        


        
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












