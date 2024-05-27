import pygame

class Rocket():
    def __init__(self, game):
        self.screen =  game.screen
        self.screen_rect = game.screen.get_rect()

        self.raw = pygame.image.load('resources/rocket1.bmp') #Superficie
        self.image = pygame.transform.scale_by(self.raw, 0.15) #Escala
        self.rect = self.image.get_rect() #Rectángulo
        self.rect.center = self.screen_rect.center #Posición

        # Store a decimal value for the ship's horizontal position.
        self.x = self.rect.x
        self.y = self.rect.y

        #Flag de movimiento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #Actualizar la posicion de la nave basado en la bandera de movimiento

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        
        if self.moving_left and self.rect.left > 0:
            self.x -= 1

        if self.moving_up and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        if self.moving_down and self.rect.top > 0:
            self.y -= 1

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        