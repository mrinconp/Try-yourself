import pygame
import sys
from settings import Settings
from shooter import Shooter
from bala import Bala

class SidewayShooter():
    def __init__(self):
        """Inicializar el juego y crear los recursos"""
        pygame.init()
        """Configuración de la pantalla"""
        
        self.settings = Settings()
        #Tamaño
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #Título
        pygame.display.set_caption("Sideway Shooter")
        #Shooter
        self.shooter = Shooter(self)
        #Balas en conjunto
        self.balas = pygame.sprite.Group()


    def run_game(self):
        """Se inicia el loop principal con un While"""
        while True:
            self._check_events()
            self.shooter.update()
            self._update_balas()
            self._update_screen()
            
    def _update_screen(self):
        #Aplicar color en cada iteración
        self.screen.fill(self.settings.bg_color)
        self.shooter.blitme()
        
        for bala in self.balas.sprites():
            bala.draw_bala()

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
        #up y down invertidos por el sistema de referencia
        if event.key == pygame.K_UP:
            self.shooter.moving_down = True
        elif event.key == pygame.K_DOWN:
            self.shooter.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._disparar_bala()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.shooter.moving_down = False
        elif event.key == pygame.K_DOWN:
            self.shooter.moving_up = False
    
    def _disparar_bala(self):
        if len(self.balas) < self.settings.balas_max:
            nueva_bala = Bala(self)
            self.balas.add(nueva_bala) 

    def _update_balas(self):
        """Actualizar posición de las balas y eliminar las que salen de la pantalla"""
        #Actualizar posición
        self.balas.update()
        #Quitar balas que salen de la pantalla
        for bala in self.balas.copy():
            if bala.rect.right >= self.settings.screen_width:
                self.balas.remove(bala)


if __name__ == '__main__':
    #Hacer una instancia con la clase y correr el juego con el metodo
    ss = SidewayShooter()
    ss.run_game()            