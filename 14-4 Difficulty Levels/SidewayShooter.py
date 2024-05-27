import pygame
import sys
from settings import Settings
from shooter import Shooter
from bala import Bala
from target import Target
from gamestats import GameStats
from boton import Boton

class SidewayShooter():
    def __init__(self):
        """Inicializar el juego y crear los recursos"""
        pygame.init()
        """Configuración de la pantalla"""
        
        self.settings = Settings()
        #Tamaño
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        #Título
        pygame.display.set_caption("Sideway Shooter")
        #Stats
        self.stats = GameStats(self)
        #Shooter
        self.shooter = Shooter(self)
        #Balas en conjunto
        self.balas = pygame.sprite.Group()
        #Target
        self.target = Target(self)
        #Botones dificultad
        self.botones_dif = []
        self._make_botones()
        

    def run_game(self):
        """Se inicia el loop principal con un While"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.shooter.update()
                self._update_balas()
                self._update_target()
            self._update_screen()
            
    def _update_screen(self):
        #Aplicar color en cada iteración
        self.screen.fill(self.settings.bg_color)
        self.shooter.blitme()
        
        for bala in self.balas.sprites():
            bala.draw_bala()

        self.target.draw_target()
        #Dibujar botones si el juego está inactivo
        if not self.stats.game_active:
            for boton in self.botones_dif:
                boton.draw_boton()
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_boton_dif(mouse_pos)

    def _check_boton_dif(self, mouse_pos):
        """Empezar el juego cuando se da click a la dificultad"""
        if not self.stats.game_active:
            for boton in self.botones_dif[:3]:
                if boton.rect.collidepoint(mouse_pos):
                    self._start_game()
                    self.settings.iniciar_config_dinamicas()
                    self._select_dif(boton.msg)
                    break

    def _make_botones(self):
        difficulties = ["facil", "dificil", "imposible"]
        offsets = [-150, 0, 150]

        for difficulty, offset in zip(difficulties, offsets):
            button = Boton(self, difficulty, (self.screen_rect.centerx, self.screen_rect.centery + offset))
            self.botones_dif.append(button)

    def _select_dif(self, msg):
        if msg == "facil":
            ...
        elif msg == "dificil":
            self.settings.shooter_speed = 2.5
            self.settings.bala_speed = 5
            self.settings.target_speed = 0.85
        elif msg == "imposible":
            self.settings.shooter_speed = 5
            self.settings.bala_speed = 8
            self.settings.target_speed = 2

    def _start_game(self):
        #Reiniciar stats
        self.stats.reset_stats()
        self.stats.game_active = True

        #Eliminar balas
        self.balas.empty()

        #Centrar target y shooter
        self.shooter.centrar_shooter()
        self.target.ubicar_target()

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
        #Quitar balas que colisionan y que salen de la pantalla
        self._check_colision_bala_target()

    def _check_colision_bala_target(self):
        for bala in self.balas.copy():
            #Si se sale de la pantalla, se falló el disparo y se debe remover la bala
            if bala.rect.colliderect(self.target.rect):
                colision = True
            else:
                colision = False

            if colision:
                self.balas.remove(bala)
                self.settings.aumentar_velocidad()

            if not colision and bala.rect.right > self.settings.screen_width:
                self._missed_shot()
                self.balas.remove(bala)
                

    def _update_target(self):
        self._check_bordes()
        self.target.update()


    def _check_bordes(self):
        """Cambio de direccion si se choca con un borde"""
        if self.target.check_bordes():
            self.settings.target_direccion *= -1

    def _missed_shot(self):
        """Respuesta a disparo fallido"""
        self.stats.balas_left -= 1
        if self.stats.balas_left == 0:
            self.stats.game_active = False


if __name__ == '__main__':
    #Hacer una instancia con la clase y correr el juego con el metodo
    ss = SidewayShooter()
    ss.run_game()            