import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Игра Толочко Егора. Enjoy it')
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
    def run_game(self):
        while True:
            self.ship.update()
    def _chek_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                        self.ship.rect.x += 1
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                self.screen.fill(self.bg_color)
                self.ship.blitme()
                pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()