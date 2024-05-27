import pygame
import sys
from time import sleep

from settings import Settings
from shooter import Shooter
from bala import Bala
from soldier import Soldier
from game_stats import GameStats

class SidewayShooter():
    def __init__(self):
        """Inicializar el juego y crear los recursos"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideway Shooter")

        self.stats = GameStats(self)
        self.shooter = Shooter(self)
        self.balas = pygame.sprite.Group()
        self.soldiers = pygame.sprite.Group()

        self._crear_ejercito()


    def run_game(self):
        """Se inicia el loop principal con un While"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.shooter.update()
                self._update_balas()
                self._update_soldiers()
            self._update_screen()

            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.shooter.blitme()

        for bala in self.balas.sprites():
            bala.draw_bala()

        self.soldiers.draw(self.screen)

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

        self._check_colisiones_bala_soldier()

    def _check_colisiones_bala_soldier(self):
        #Revisar colisiones y borrar soldado dado el caso
            #Los dos argumentos True borran los elementos que colisionan
        collisions = pygame.sprite.groupcollide(
            self.balas, self.soldiers, True, True)
        
        if not self.soldiers:
            #Eliminar balas existentes y crear nuevo ejercito
            self.balas.empty()
            self._crear_ejercito()

    def _update_soldiers(self):
        self._check_ejercito_bordes()
        self.soldiers.update()

        if pygame.sprite.spritecollideany(self.shooter, self.soldiers):
            self._soldier_reached()

        self._check_soldiers_margin()


    def _crear_ejercito(self):
        #Alien de referencia para medidas, no para incluir en la ejercito
        soldier = Soldier(self)
        soldier_width, soldier_height = soldier.rect.size 
        espacio_disponible_y = self.settings.screen_height - soldier_height
        numero_soldados_y = espacio_disponible_y // (2*soldier_height)

        #Determinar el número de columnas
        shooter_width = self.shooter.rect.width
        espacio_disponible_x = (self.settings.screen_width - 
                                shooter_width)
        numero_columnas = espacio_disponible_x // (2*soldier_width)
    
        #Crear ejercito
        for numero_col in range(numero_columnas):
            for soldier_number in range(numero_soldados_y):
                #Crear un soldado y posicionarlo
                self._create_soldier(soldier_number, numero_col)

    def _create_soldier(self, soldier_number, numero_col):
        soldier = Soldier(self)
        soldier_width, soldier_height = soldier.rect.size

        #Coordenadas del rectángulo donde se va a posicionar
        soldier.x = (self.settings.screen_width - 2*soldier_width
                     - soldier_width*numero_col)
        soldier.rect.x = soldier.x
        soldier.y = soldier_height + soldier_height*soldier_number
        soldier.rect.y = soldier.y

        self.soldiers.add(soldier)

    def _check_ejercito_bordes(self):
        for soldier in self.soldiers.sprites():
            if soldier.check_bordes():
                self._cambiar_direccion()
                break

    def _cambiar_direccion(self):
        """Acercar el ejercito y cambiar la direccion"""
        for soldier in self.soldiers.sprites():
            soldier.rect.x -= self.settings.ejercito_move_speed
        self.settings.ejercito_direccion *= -1

    def _soldier_reached(self):
        self.stats.lives_left -= 1
        if self.stats.lives_left >0:

            self.soldiers.empty()
            self.balas.empty()

            self._crear_ejercito()
            self.shooter.centrar_shooter()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
                     
    def _check_soldiers_margin(self):
        for soldier in self.soldiers.sprites():
            if soldier.rect.left <= 0:
                self._soldier_reached()
                break


if __name__ == '__main__':
    #Hacer una instancia con la clase y correr el juego con el metodo
    ss = SidewayShooter()
    ss.run_game()            