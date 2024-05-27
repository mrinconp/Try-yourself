import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Una clase para las balas que dispara el shooter"""
    def __init__(self, ai_game):
        """Crear un objeto 'bala' y posicionarlo"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bala_color

        #Rectángulo en (0,0) y luego se ubica
        self.rect = pygame.Rect(0,0, self.settings.bala_width, self.settings.bala_height)
        self.rect.midright = ai_game.shooter.rect.midright

        #Guardar la posición como un decimal
        self.x = float(self.rect.x)

    def update(self):
        #Mover la bala hacia la derecha
        self.x += self.settings.bala_speed

        #Actualizar posición
        self.rect.x = self.x
    
    def draw_bala(self):
        #Dibujar la bala en la pantalla
        pygame.draw.rect(self.screen, self.color, self.rect)