import pygame
from pygame.sprite import Sprite


class Gota(Sprite):
    """Una clase para configurar las gotas"""

    def __init__(self, game):
        """Crear la gota y posicionarla"""
        super().__init__()

        self.screen = game.screen
        self.screen_height = game.screen_heigth

        #Cargar la imagen de la nave y su rectangulo
        self.raw = pygame.image.load('resources/gota1.bmp')
        self.image = pygame.transform.scale_by(self.raw, 0.1)
        self.rect = self.image.get_rect()

        #Iniciar cada Gota arriba a la izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Guardar la posición inicial exacta
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def _check_borde(self):
        if self.rect.top >= self.screen_height:
            return True
        
    def update(self):
        if self.rect.top >= self.screen_height:
            self.rect.y = 0
        else:
            #Mover hacia abajo
            self.rect.y += 1