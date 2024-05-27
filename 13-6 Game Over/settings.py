class Settings():
    """Establecer las configuraciones del juego"""
    
    def __init__(self):
        """Inicializar las configuraciones del juego"""
        #Configuraciones de pantalla:
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #Congig shooter
        self.shooter_speed = 0.7
        self.max_lives = 3

        #Config balas
        self.bala_speed = 1.0
        self.bala_width = 5
        self.bala_height = 5
        self.bala_color = (60,60,60)
        self.balas_max = 3

        #Config soldier
        self.soldier_speed = 0.4 #y_speed
        self.ejercito_move_speed = 50 #x_speed
        #Direccion(1 abajo, -1 arriba)
        self.ejercito_direccion = 1
        