import pygame.font


class Scoreboard():
    """display the scoreboard"""
    def __init__(self, game_settings, screen, stats):
        """initialize the scoreboard"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        # font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # the image for scoring
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)

        # locate the scoreboard at the up right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """display the score"""
        self.screen.blit(self.score_image, self.score_rect)

