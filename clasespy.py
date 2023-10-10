from var import *
import pygame

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
        
