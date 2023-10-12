import pygame
from jugador import (Jugador, objetopy)
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a, K_SPACE)
from var import (size, ancho, alto)
from background import Background
from plataformas import Plataforma
from botones import Boton_palay
import random
class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.ventana = pygame.display.set_mode(size)
        pygame.display.set_caption("PY GAME")
        self.limitfps = pygame.time.Clock()
        self.initialize()

    def initialize(self):
        self.all = pygame.sprite.Group()
        self.fondo = pygame.sprite.Group()
        self.plataformas= pygame.sprite.Group()
        self.jugador1 = Jugador()
        #self.botonplay1 = Boton_palay(100, 100, 50, 50)
        #self.all.add(self.botonplay1)
        self.plataforma = Plataforma(ancho, ancho/2, 600)
        self.all.add(self.plataforma)
        self.plataformas.add(self.plataforma)
        self.background1 = Background(True, 20, "2", 0)
        self.background2 = Background(False, 50, "3", 40)
        self.fondo.add(self.background1)
        self.fondo.add(self.background2)
        self.all.add(self.jugador1)

        #====init controles externos
        self.pressed_space = False
        #======

        
        
        
        self.dist_primeraplataforma = random.randint(90, 280)
        self.ancho_plataforma_anterior = None
        self.proximaplataforma = None
        self.fps = 60

        self.run = True
        self.salir = False 

        self.last_time = pygame.time.get_ticks()  # Guardar el tiempo del último ciclo

    def menurun(self):
        while self.run:
            self.event()
            self.update(True)
            self.colisiones()
            self.render()
            if self.pressed_space:
                break
            self.limitfps.tick(60)
        self.mainrun()
        return self.salir


       
    def mainrun(self):
        while self.run:
            self.event()
            self.agregarplataformas()
            self.update()
            self.colisiones()
            #self.statusobjet()
            self.render()
            print(len(self.plataformas))
            
            self.limitfps.tick(60)
        return self.salir
        

    def update(self, inicio = False):
        current_time = pygame.time.get_ticks()  # Tiempo actual
        delta_time = (current_time - self.last_time) / 1000.0  # Calcular delta_time en segundos
        self.last_time = current_time  # Actualizar el tiempo del último ciclo

        
        if not inicio:
            self.plataformas.update()
            self.jugador1.update()
        else:
            self.jugador1.update(True)
        self.fondo.update(delta_time)

    def render(self):
        self.ventana.fill((200, 200, 255))
        for backgroundlol in self.fondo:
            backgroundlol.render(self.ventana)
        self.all.draw(self.ventana)
        
        pygame.display.flip()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.run=False
               self.salir = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.run=False
                    self.salir = True
                if event.key == K_SPACE:
                    self.pressed_space = True
                else:
                    self.pressed_space = False
            
    
    def agregarplataformas(self):
        if not self.ancho_plataforma_anterior:
            print("holadfkjlfdsljkfdsklj", self.dist_primeraplataforma)
            self.dist_primeraplataforma -= 4
            if self.dist_primeraplataforma <= 0:

                self.newplataforma()
        
        elif self.ancho_plataforma_anterior and self.proximaplataforma <= 0:

            self.newplataforma()
        if self.proximaplataforma:
            self.proximaplataforma -= 4

    
    def newplataforma(self):
            
            distancia_maxima = 350
            newancho = random.randint(70, 500)
            x = ancho + newancho//2
            newalto = random.randint(450,alto-50)
            self.plataforma1 = Plataforma(newancho, x, newalto)
             
            self.all.add(self.plataforma1)
            self.plataformas.add(self.plataforma1)
            self.ancho_plataforma_anterior = newancho
            self.proximaplataforma = random.randint(newancho+60, newancho+distancia_maxima)



    def colisiones(self):
        suelo = pygame.sprite.spritecollideany(self.jugador1, self.plataformas)
        if suelo:

            upupdist = self.jugador1.rect.top - suelo.rect.top
            updowndist = self.jugador1.rect.bottom - suelo.rect.top
            #print(upupdist, updowndist)
            
            if not upupdist>0 and updowndist<35  :
                #print(self.jugador1.rect.right-10, suelo.rect.left, "      ",self.jugador1.rect.left-10, suelo.rect.right)
                if  self.jugador1.rect.right-10 > suelo.rect.left:
                    
                    print(("se  logro"))
                    self.jugador1.posy -= self.jugador1.rect.bottom  - suelo.rect.top 
                    self.jugador1.savepos()
                    self.jugador1.obtenerpisoinfo(suelo)
                    self.jugador1.vely = 0
                    self.jugador1.sueloartificial = True
                    self.jugador1.cantidad_salto = 1
                    #print(self.jugador1.rect.bottom  - suelo.rect.top)

            elif suelo.rect.bottom- self.jugador1.rect.top < 15:
                self.jugador1.posy +=  suelo.rect.bottom -self.jugador1.rect.top
                self.jugador1.vely = 0
            distancialeft = self.jugador1.rect.right - suelo.rect.left
            distanciarigth = self.jugador1.rect.left - suelo.rect.left
            

            if not distanciarigth>0 and distancialeft <10:
                self.jugador1.posx -= self.jugador1.rect.right - suelo.rect.left
                self.jugador1.velx = 0


            distancialeft = suelo.rect.right-self.jugador1.rect.right 
            distanciarigth =suelo.rect.right- self.jugador1.rect.left 

            if not distancialeft >0 and distanciarigth <10:
          
                self.jugador1.posx += suelo.rect.right - self.jugador1.rect.left
                self.jugador1.velx = 0


   
    def statusobjet(self):
        if self.jugador1.statuskill():
            print("hello")
            self.run = False
    
    def salirgame(self):
        pygame.quit()

