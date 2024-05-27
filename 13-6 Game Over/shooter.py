import pygame

class Shooter():
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        #Imagen shooter y su rectángulo
        self.raw = pygame.image.load('resources/shooter1.bmp')
        self.image = pygame.transform.scale_by(self.raw, 0.15) #Escala
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = self.rect.y

        self.moving_up = False
        self.moving_down = False

    def update(self):
        #Actualizar la posicion de la nave basado en la bandera de movimiento

        if self.moving_up and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.shooter_speed

        if self.moving_down and self.rect.top > 0:
            self.y -= self.settings.shooter_speed

        self.rect.y = self.y


    def blitme(self):
        """Dibujar la nave en su posición"""
        self.screen.blit(self.image, self.rect)

    def centrar_shooter(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = self.rect.y