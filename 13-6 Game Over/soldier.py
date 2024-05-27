import pygame
from pygame.sprite import Sprite


class Soldier(Sprite):
    """Una clase para configurar los Soldiers"""

    def __init__(self, game):
        """Crear el Soldier y posicionarlo"""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        #Cargar la imagen de la nave y su rectangulo
        self.raw = pygame.image.load('resources/soldier1.bmp')
        self.image = pygame.transform.scale_by(self.raw, 0.1)
        self.rect = self.image.get_rect()

        #Iniciar cada Soldier arriba a la izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Guardar la posición inicial exacta
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Mover el soldado hacia arriba o hacia abajo"""
        self.y += (self.settings.soldier_speed * self.settings.ejercito_direccion)
        self.rect.y = self.y

    def check_bordes(self):
        """True si un soldier toca un borde de la pantalla"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True