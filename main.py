import pygame
import sys
from constants import *


def handle_close_btn():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("X button pressed - exiting the game")
            pygame.quit()
            sys.exit()


def play():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        handle_close_btn()
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()


def main():
    pygame.init()
    print("Starting asteroids!")
    play()


if __name__ == "__main__":
    main()
