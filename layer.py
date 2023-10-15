from botones import (Boton_play, texto1, FondoTransparente)
import pygame 
from constantes import *

"""layer es el que va a controlar botones
  y textos que apareceran en el menu de pausa y el de comenzar
tambien sera el encargado de manejar los textos 
mientras se ejecuta el main run, como el score"""
class layers():
    def __init__(self) -> None:
        self.menulayer = pygame.sprite.Group()
        self.pausalayer = pygame.sprite.Group()
        self.mainrun = pygame.sprite.Group()

        self.pausa = False
        self.menu = True
        self.main = False

        self.pressed_play = False
        self.pressed_opciones = False
        self.pressed_salir = False
        self.pressed_continuar = False
        
        self.initmenu()
        self.initpausa()

    def update(self):
        if self.menu:
            self.menulayer.update()

            self.pressed_play = self.botonplay.botonpresionado()

            self.pressed_salir = self.botonsalir.botonpresionado()
         
        if self.pausa:
            self.pausalayer.update()
            self.pressed_salir = self.botonsalir2.botonpresionado()
            self.pressed_continuar = self.botoncontinuar.botonpresionado()
        if self.main:
            self.mainrun.update()

    def draw(self, ventana):
        if self.menu:
            self.menulayer.draw(ventana)
        if self.pausa:
            self.pausalayer.draw(ventana)
        if self.main:
            self.mainrun.draw(ventana)


    def initpausa(self):
        self.backgraund = FondoTransparente(ANCHO/2, ALTO/2, ANCHO, ALTO, 35)
        self.textopausa = texto1(ANCHO/2, ALTO/4, 80, "Pausa", isboton= False)
        self.botoncontinuar = texto1(ANCHO/2, ALTO/1.8, 50, "continuar", isboton= True,)
        self.botonsalir2 = texto1(ANCHO/2, ALTO/1.4, 30, "salir", isboton= True,)
        self.pausalayer.add(self.backgraund)
        self.pausalayer.add(self.textopausa)
        self.pausalayer.add(self.botonsalir2)
        self.pausalayer.add(self.botoncontinuar)
    def initmenu(self):
        self.botonplay = texto1(ANCHO/2, ALTO/2.3, 50, "Jugar", isboton= True,)
        self.botonoption = texto1(ANCHO/2, ALTO/1.7, 40, "configuraciones", isboton= True,)
        self.botonsalir = texto1(ANCHO/2, ALTO/1.4, 30, "salir", isboton= True,)
        self.menulayer.add(self.botonplay)
        self.menulayer.add(self.botonsalir)
        self.menulayer.add(self.botonoption)
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
    def playpresionado(self):
        return self.pressed_play
    def salirpresionado(self):
        return self.pressed_salir
    def continuarpresionado(self):
        return self.pressed_continuar
    
    


    

