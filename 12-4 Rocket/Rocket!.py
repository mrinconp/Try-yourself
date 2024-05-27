import pygame
import sys
from rocket import Rocket


class Rocket_game():
    def __init__(self):
        """Inicializar el juego y crear los recursos"""
        pygame.init()
        """Configuración de la pantalla"""
        #Tamaño
        self.screen = pygame.display.set_mode((1200,800))
        #Título
        pygame.display.set_caption("Rocket!")
        #Color fondo
        self.bg_color = (0,0,0)
        #Rocket
        self.rocket = Rocket(self)

    def run_game(self):
        """Se inicia el loop principal con un While"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            
    def _update_screen(self):
        #Aplicar color en cada iteración
        self.screen.fill(self.bg_color)
        self.rocket.blitme()

        #Actualizar y hacer visible la pantalla
        pygame.display.flip()
    
    def _check_events(self):
        #Event loop para registrar eventos(acciones) del teclado y mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type ==pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True

        #up y down invertidos por el sistema de referencia
        if event.key == pygame.K_UP:
            self.rocket.moving_down = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False

        if event.key == pygame.K_UP:
            self.rocket.moving_down = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_up = False


if __name__ == '__main__':
    #Hacer una instancia con la clase y correr el juego con el metodo
    ro = Rocket_game()
    ro.run_game()            