from constantes import *
import pygame
from clasespy import objetopy
import os


class Botones(objetopy):
    def __init__(self,  x, y):
        super().__init__(x, y)

        self.boton_pressed = False

    def initimage(self, dir, nameimage, tamaño):
        imagen_path = os.path.join(dir, nameimage)  # Unir el directorio con el nombre del archivo
        self.image = pygame.image.load(imagen_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tamaño*2, tamaño*2))



    def botonpresionado(self):
        return self.boton_pressed
    def detectarclik(self):
        mauscliks = pygame.mouse.get_pressed()  # Obtiene el estado de los botones del ratón

        if mauscliks[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.boton_pressed = True
        else:
            self.boton_pressed = False
        

class Boton_play(Botones):
    def __init__(self,  x, y, tamaño):
        super().__init__(x, y)
        self.initimage("sprites/", "botonplay1.png", tamaño)
        self.initrect()

    def update(self):
        self.detectarclik()

class texto1(Botones):
    def __init__(self,  x, y, tamaño, contenido, color =(255, 255, 255), 
             isboton = False, animacion = False ):
        super().__init__(x, y)
        self.isboton = isboton
        self.animacion = animacion

        self.fondo_transparente = False
        self.color = color
        self.tamaño = tamaño
        self.contenido = contenido
        self.trasparencia =40
        self.actualizar_texto(contenido)  # Llama a la función para crear el texto
           

    def actualizar_texto(self, contenido):
        font = pygame.font.SysFont("Arial", self.tamaño, True, False)

        if self.fondo_transparente:
            texto_superficie = font.render(contenido, True, self.color)
            image = pygame.Surface((texto_superficie.get_width(), texto_superficie.get_height()), pygame.SRCALPHA)
            image.fill((0, 0, 0, self.trasparencia)) 
    
            # Superponer la superficie de texto en la parte superior del fondo semitransparente
            image.blit(texto_superficie, (0, 0))
        else:
            image = font.render(contenido, True, self.color)  # Sin fondo transparente

        self.image = image
        self.initrect()

    def cambiar_fondo_transparente(self, fondo_transparente):
        self.fondo_transparente = fondo_transparente
        self.actualizar_texto(self.contenido)  # Actualizar el tex

    def update(self):
        if self.isboton:
            self.detectarclik()
            
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.cambiar_fondo_transparente(True)
            else:
                self.cambiar_fondo_transparente(False)

class FondoTransparente(objetopy):
    def __init__(self, x, y, ancho, alto, transparencia):
        super().__init__(x, y)

        # Crear una superficie con canal alfa
        self.image = pygame.Surface((ancho, alto), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, transparencia))  # Rellena con blanco y la transparencia deseada

        self.initrect()

            
