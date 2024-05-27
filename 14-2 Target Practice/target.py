import pygame

class Target():
    def __init__(self, game):
        """Iniciar los atributos del rectángulo"""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        #Establecer las dimensiones y propiedades del rectángulo
        self.width, self.height = 50,100
        self.color_boton = (0,0,140)

        #Construir el rectángulo y ubicarlo
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.topright = self.screen_rect.topright

        self.y = float(self.rect.y)

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color_boton, self.rect)

    def update(self):
        """Mover el rectángulo hacia arriba o hacia abajo"""
        self.y += (self.settings.target_speed * self.settings.target_direccion)
        self.rect.y = self.y

    def check_bordes(self):
        """True si el rectangulo toca un borde"""
        self.screen_rect = self.screen.get_rect()
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top < 0:
            return True
    
    def ubicar_target(self):
        self.rect.topright = self.screen_rect.topright
        self.y = float(self.rect.y)