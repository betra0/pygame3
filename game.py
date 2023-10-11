import pygame
from jugador import (Jugador, objetopy)
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a, K_SPACE)
from var import (size)
from background import Background
from plataformas import Plataforma
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
        self.plataforma = Plataforma(400, 600, 500)

        self.all.add(self.plataforma)
        self.plataformas.add(self.plataforma)
    
        
        self.background1 = Background(True, 20, "2", 0)
        self.background2 = Background(False, 50, "3", 40)
        self.fondo.add(self.background1)
        self.fondo.add(self.background2)
        
        self.all.add(self.jugador1)
        

        self.fps = 60

        self.run = True

        self.last_time = pygame.time.get_ticks()  # Guardar el tiempo del último ciclo

        
    def mainrun(self):
        while self.run:
            self.event()
            self.update()
            self.colisiones()
            self.render()
            

            self.limitfps.tick(60)
        
        pygame.quit()

    def update(self):
        current_time = pygame.time.get_ticks()  # Tiempo actual
        delta_time = (current_time - self.last_time) / 1000.0  # Calcular delta_time en segundos
        self.last_time = current_time  # Actualizar el tiempo del último ciclo

        self.all.update()
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


        











            # Colisión en el lado derecho
           #if suelo.rect.left < self.jugador1.rect.right:
           #    self.jugador1.posx += suelo.rect.right - self.jugador1.rect.left
           #    self.jugador1.velx = 0

        
