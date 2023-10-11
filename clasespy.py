from var import *
import pygame

class objetopy(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.posx, self.posy = x, y
        self.tamaño = tamaño_player
        self.image = pygame.Surface((self.tamaño, self.tamaño))
        self.image.fill((100, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.posx, self.posy 

        self.sueloartificial = False
        self.fricion = 0.5
        self.velocidad = 18
        self.gravedad = 0.5
        self.velx = 0
        self.vely = 0
    
    def initrect(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.posx, self.posy


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
        if not self.isonfloor(6):
            self.vely += self.gravedad
    def isonfloor(self, n = 0):
        retorno = False
        if not self.sueloartificial :
        
            if self.posy+self.tamaño/2+n >= alto:
                retorno = True
        else:
            retorno = True
        
        return retorno
    
    def simularfricionx(self,):
        fricion=self.fricion
        if fricion > abs(self.velx):
            fricion = abs(self.velx)
            
        if self.velx > 0:
            self.velx -= fricion
            
        elif self.velx  < 0:
            self.velx += fricion

        
