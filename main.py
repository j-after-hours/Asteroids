import pygame
import sys
from constants import *
from player import Player


def handle_close_btn():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("X button pressed - exiting the game")
            pygame.quit()
            sys.exit()


def handle_updatable(updatable, dt):
    for obj in updatable:
        obj.update(dt)


def handle_drawable(drawable, screen):
    for obj in drawable:
        obj.draw(screen)


def play():
    # prepare screen for display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
    # create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # add the player to both groups
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # initialize clock object
    clock = pygame.time.Clock()
    dt = 0

    while True:
        handle_close_btn()

        pygame.Surface.fill(screen, "black")
        handle_updatable(updatable, dt)
        handle_drawable(drawable, screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


def main():
    pygame.init()
    print("Starting asteroids!")
    play()


if __name__ == "__main__":
    main()
