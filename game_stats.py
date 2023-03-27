class GameStats():
    """track the stats in the game"""
    def __init__(self, game_settings):
        """initialize the stats"""
        self.game_settings = game_settings
        self.reset_stats()

        # inactive at the beginning of game
        self.game_active = False

        # the best score
        self.high_score = 0

    def reset_stats(self):
        """initialize stats that will change during the game"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1

