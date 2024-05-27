import pygame

class Duck():
    def __init__(self, game):
        self.screen =  game.screen
        self.screen_rect = game.screen.get_rect()

        self.raw = pygame.image.load('resources/duck1.bmp') #Superficie
        self.image = pygame.transform.scale_by(self.raw, 0.5) #Escala
        self.rect = self.image.get_rect() #Rectángulo
        
        #Atributo fondo de la imagen
        self.backg_color = pygame.Surface.get_at(self.image, (self.rect.x, self.rect.y))
        
        self.rect.center = self.screen_rect.center #Posición

    def blitme(self):
        self.screen.blit(self.image, self.rect)