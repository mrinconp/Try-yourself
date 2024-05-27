import pygame
import sys


class Keys_printing():
    def __init__(self):
        """Inicializar el juego y crear los recursos"""
        pygame.init()
        """Configuración de la pantalla"""
        #Tamaño
        self.screen = pygame.display.set_mode((800,600))
        #Título
        pygame.display.set_caption("Keys")
        #Color fondo
        self.bg_color = (0,0,0)

    def run_game(self):
        """Se inicia el loop principal con un While"""
        while True:
            self._check_events()
            self._update_screen()
            
    def _update_screen(self):
        #Aplicar color en cada iteración
        self.screen.fill(self.bg_color)

        #Actualizar y hacer visible la pantalla
        pygame.display.flip()
    
    def _check_events(self):
        #Event loop para registrar eventos(acciones) del teclado y mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                #Imprimir el atributo event.key:
                elif event.type ==pygame.KEYDOWN:
                    print(event.key)


if __name__ == '__main__':
    #Hacer una instancia con la clase y correr el juego con el metodo
    ks = Keys_printing()
    ks.run_game()            