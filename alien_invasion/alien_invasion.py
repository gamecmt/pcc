import sys
import pygame
import settings


def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alen Invasion")

    # set background color
    bg_color = (230, 230, 230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # every loop refill screen
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()

run_game()
