import pygame
import sys
from raindrop import Gota

class Rain():
    def __init__(self):
        """Inicializar el juego y crear los recursos"""
        pygame.init()
        """Configuración de la pantalla"""
        #Tamaño
        self.screen_width = 1200
        self.screen_heigth = 800
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_heigth))
        #Título
        pygame.display.set_caption("Rain")
        #Color fondo
        self.bg_color = (230,230,230)

        #Gotas
        self.gotas = pygame.sprite.Group()
        self._hacer_lluvia()

    def run_game(self):
        """Se inicia el loop principal con un While"""
        while True:
            self._check_events()
            self._update_gotas()
            self._update_screen()
            
    def _update_screen(self):
        #Aplicar color en cada iteración
        self.screen.fill(self.bg_color)
        
        self.gotas.draw(self.screen)

        #Actualizar y hacer visible la pantalla
        pygame.display.flip()
    
    def _check_events(self):
        #Event loop para registrar eventos(acciones) del teclado y mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

    def _hacer_lluvia(self):
        gota = Gota(self)
        gota_width = gota.rect.x
        espacio_disponible_x = self.screen_width - (2*gota_width)
        numero_gotas_x = espacio_disponible_x // (2*gota_width)

        for numero_gota in range(numero_gotas_x):
            #Crear gota y posicionarla
            self._crear_gota(numero_gota)

    def _crear_gota(self, numero_gota):
        gota = Gota(self)
        gota_width= gota.rect.x

        #Coordenadas del rectángulo donde se va a posicionar
        gota.x = gota_width + 2*gota_width*numero_gota
        gota.rect.x = gota.x
        self.gotas.add(gota)

    def _update_gotas(self):
        self.gotas.update()
        

if __name__ == '__main__':
    #Hacer una instancia con la clase y correr el juego con el metodo
    rn = Rain()
    rn.run_game()            