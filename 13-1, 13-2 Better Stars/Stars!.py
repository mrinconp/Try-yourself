import pygame
import sys
from star import Star
import random


class Stars():
    def __init__(self):
        """Inicializar el juego y crear los recursos"""
        pygame.init()
        """Configuración de la pantalla"""
        #Tamaño
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        #Título
        pygame.display.set_caption("Keys")
        #Color fondo
        self.bg_color = (0,0,0)
        #Estrellas
        self.cantidad_estrellas = 100
        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        """Se inicia el loop principal con un While"""
        while True:
            self._check_events()
            self._update_screen()
            
    def _update_screen(self):
        #Aplicar color en cada iteración
        self.screen.fill(self.bg_color)

        self.stars.draw(self.screen)
        #Actualizar y hacer visible la pantalla
        pygame.display.flip()
    
    def _check_events(self):
        #Event loop para registrar eventos(acciones) del teclado y mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                #Imprimir el atributo event.key:
                elif event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

    def _create_stars(self):
        """Crear estrellas de forma aleatoria"""
        x_values = random.sample(range(self.screen_width), self.cantidad_estrellas)
        y_values = random.sample(range(self.screen_height), self.cantidad_estrellas)

        for i in range(self.cantidad_estrellas):
            x = x_values[i]
            y = y_values[i]
            self._create_star(x, y)

    def _create_star(self, x, y):
        star = Star(self)

        star.rect.x = x
        star.rect.y = y
        self.stars.add(star)
        



if __name__ == '__main__':
    #Hacer una instancia con la clase y correr el juego con el metodo
    st = Stars()
    st.run_game()            