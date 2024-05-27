class Settings():
    """Establecer las configuraciones del juego"""
    
    def __init__(self):
        """Inicializar las configuraciones del juego"""
        #Configuraciones de pantalla:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Velocidad shooter
        self.shooter_speed = 1.5

        #Config balas
        self.bala_speed = 1.0
        self.bala_width = 5
        self.bala_height = 5
        self.bala_color = (60,60,60)
        self.balas_max = 3

        #Config target
        self.target_speed = 0.5
        #Direccion(1 abajo, -1 arriba)
        self.target_direccion = 1