import sys
import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alen Invasion")

    # set background color
    bg_color = (230, 230, 230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # every loop refill screen
        screen.fill(bg_color)
        pygame.display.flip()

run_game()
