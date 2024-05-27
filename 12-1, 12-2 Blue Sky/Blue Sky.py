import pygame
import sys
from duck import Duck

class My_game():
    def __init__(self):
        """Inicializar el juego y crear los recursos"""
        pygame.init()
        """Configuración de la pantalla"""
        #Tamaño
        self.screen = pygame.display.set_mode((1200,800))
        #Título
        pygame.display.set_caption("Blue Sky")
        
        #Duck como un atributo de My_game:
        self.duck = Duck(self)

        #Color fondo
        self.bg_color =  self.duck.backg_color

    def run_my_game(self):
        while True:
            #Reconocer cuando se cierra la ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Pintar la superficie 'screen'
            self.screen.fill(self.bg_color)
            #Mostrar Duck
            self.duck.blitme()
            #Actualizar pantalla
            pygame.display.flip()

if __name__ == '__main__':
    #Hacer una instancia con la clase y correr el juego
    bs = My_game()
    bs.run_my_game()

"""Nota:
Es posible llamar la función fill() con un color RGB como argumento directamente, pero tiene más sentido asignar el color como un atributo de la instancia.
"""
   