import pygame
from jugador import (Jugador, objetopy)
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, 
            K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_d, K_a, K_SPACE)
from var import (size)
from background import Background
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
        self.jugador1 = Jugador()
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
            self.render()
            

            self.limitfps.tick(self.fps)
        
        pygame.quit()

    def update(self):
        current_time = pygame.time.get_ticks()  # Tiempo actual
        delta_time = (current_time - self.last_time) / 1000.0  # Calcular delta_time en segundos
        self.last_time = current_time  # Actualizar el tiempo del último ciclo

        self.all.update()
        self.fondo.update(delta_time)
        

        pass

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