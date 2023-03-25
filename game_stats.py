class GameStats():
    """track the stats in the game"""
    def __init__(self, game_settings):
        """initialize the stats"""
        self.game_settings = game_settings
        self.reset_stats()
        self.game_active = True


    def reset_stats(self):
        """initialize stats that will change during the game"""
        self.ships_left = self.game_settings.ship_limit