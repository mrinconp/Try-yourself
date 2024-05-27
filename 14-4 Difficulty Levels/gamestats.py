class GameStats():
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()
        #Iniciar el juego en un estado inactivo
        self.game_active = False

    def reset_stats(self):
        """Iniciar estadísticas que pueden cambiar durante el juego"""
        self.balas_left = self.settings.balas_max