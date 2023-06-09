import pygame.font
from pygame.sprite import  Group

from ship import  Ship


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
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        # score_str = str(self.stats.score)
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)

        # locate the scoreboard at the up right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_level(self):
        """display the level"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,
                                            self.game_settings.bg_color)

        # locate the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """display the score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # display ships
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """display the best score"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                                  self.game_settings.bg_color)

        # locate the best score in the up middle
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_ships(self):
        # display the remaining ships
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)



