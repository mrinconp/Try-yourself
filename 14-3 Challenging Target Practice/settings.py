class Settings():
    """Establecer las configuraciones del juego"""
    
    def __init__(self):
        """Inicializar las configuraciones constantes del juego"""
        #Configuraciones de pantalla:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Config balas
        self.bala_width = 5
        self.bala_height = 5
        self.bala_color = (60,60,60)
        self.balas_max = 3

        #Tasa de aumento de velocidad
        self.aumento_vel_escala = 1.3

        self.iniciar_config_dinamicas()

    def iniciar_config_dinamicas(self):
        
        #Velocidad shooter
        self.shooter_speed = 1.5
        #Velocidad balas
        self.bala_speed = 3.0
        #Config target
        self.target_speed = 0.5
        #Direccion(1 abajo, -1 arriba)
        self.target_direccion = 1

    def aumentar_velocidad(self):
        #Velocidad shooter
        self.shooter_speed *= self.aumento_vel_escala
        #Velocidad balas
        self.bala_speed  *= self.aumento_vel_escala
        #Velocidad target
        self.target_speed *= self.aumento_vel_escala