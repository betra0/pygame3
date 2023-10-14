from botones import Boton_play
import pygame 
from constantes import *

"""layer es el que va a controlar botones
  y textos que apareceran en el menu de pausa y el de comenzar
tambien sera el encargado de manejar los textos 
mientras se ejecuta el main run, como el score"""
class layers():
    def __init__(self) -> None:
        self.botones = pygame.sprite.Group()
        self.menulayer = pygame.sprite.Group()
        self.pausalayer = pygame.sprite.Group()
        self.mainrun = pygame.sprite.Group()

        self.pausa = False
        self.menu = True
        self.main = False
        
        self.initmenu()
    def initpausa(self):
        pass
    def initmenu(self):
        self.botonplay = Boton_play(ANCHO/2, ALTO/2, 50)
        self.menulayer.add(self.botonplay)
    def initmainrun(self):
        pass
    def pausaon(self):
        self.pausa = True
        pass
    def pausaoff(self):
        self.pausa = False
    def mainon(self):
        self.main = True
    def mainoff(self):
        self.main = False
    def menuoff(self):
        self.menu = False
    

    def update(self):
        if self.menu:
            self.menulayer.update()
        if self.pausa:
            self.pausalayer.update()
        if self.main:
            self.mainrun.update()
        pass
    def draw(self, ventana):
        if self.menu:
            self.menulayer.draw(ventana)
        if self.pausa:
            self.pausalayer.draw(ventana)
        if self.main:
            self.mainrun.draw(ventana)