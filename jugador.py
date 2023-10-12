from var import *
import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a, K_SPACE)
from clasespy import objetopy

        
class Jugador(objetopy):
    def __init__(self):

        super().__init__(400, 300)
        self.image.fill((255, 180, 200))
        self.salto_presionado = False
        self.salto= False
        self.nosalto =True
        self.cantidad_salto = 1
        self.en_el_suelo = False  # Variable para rastrear si el jugador está en el suelo
        self.pisoinfo = None
        self.impulso_salto = 9
        
        

    def update(self, bloq_movimiento = False):
        keys = pygame.key.get_pressed()
        if not bloq_movimiento:
            if keys[K_d]:
                self.velx = 0.1
            if keys[K_a]:
                self.velx = -0.1
            if keys[K_w] or keys[K_SPACE]:
                self.salto_presionado = True
            else:
               self.salto_presionado = False
    
            if self.salto_presionado and not self.salto and self.nosalto:
                self.salto = True
                self.nosalto = False
    
            if not self.salto_presionado:
                self.nosalto = True
    
            if self.salto and self.isonfloor(8):
                self.vely = -self.impulso_salto
            elif self.salto and not self.isonfloor(8) and self.cantidad_salto >= 1:
                self.vely = -self.impulso_salto/1.15
                self.cantidad_salto -=1
            elif not self.salto and self.isonfloor(8):
                self.cantidad_salto = 1
    
       
        self.simulargravedad()
        self.velpos(self.velx, self.vely)
        self.simularfricionx()
        self.killxlimit()
        self.salto = False
        if self.pisoinfo:
            self.pisoartificial()

    def pisoartificial(self,):
        suelo = self.pisoinfo
        #print("jeje")
        
        xleft, xright, ytop = suelo.rect.left, suelo.rect.right, suelo.rect.top
        if self.rect.bottom < ytop:
            self.sueloartificial = False
            self.pisoinfo = False
        if self.rect.right-10 < xleft:
            self.sueloartificial = False
            self.pisoinfo = False

        if self.rect.left+10 > xright:
            self.sueloartificial = False
            self.pisoinfo = False


        pass

    def obtenerpisoinfo(self, piso):
        self.pisoinfo = piso












