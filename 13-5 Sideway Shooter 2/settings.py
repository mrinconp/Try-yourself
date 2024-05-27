class Settings():
    """Establecer las configuraciones del juego"""
    
    def __init__(self):
        """Inicializar las configuraciones del juego"""
        #Configuraciones de pantalla:
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #Velocidad shooter
        self.shooter_speed = 0.7

        #Config balas
        self.bala_speed = 1.0
        self.bala_width = 5
        self.bala_height = 5
        self.bala_color = (60,60,60)
        self.balas_max = 3

        #Config soldier
        self.soldier_speed = 0.4
        self.manada_move_speed = 15
        #Direccion(1 abajo, -1 arriba)
        self.manada_direction = 1