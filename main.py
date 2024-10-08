import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def handle_close_btn():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("X button pressed - exiting the game")
            pygame.quit()
            sys.exit()


def handle_updatable(updatable, dt):
    for obj in updatable:
        obj.update(dt)


def handle_collisions(asteroids, player, shots):
    for asteroid in asteroids:
        if asteroid.collides_with(player):
            print("Game over!")
            pygame.quit()
            sys.exit()

        for shot in shots:
            if asteroid.collides_with(shot):
                asteroid.split()
                shot.kill()


def handle_drawable(drawable, screen):
    for obj in drawable:
        obj.draw(screen)


def play():
    # prepare screen for display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
    # create sprite groups
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()

    # add the player to both groups
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # add the asteroids to both groups as well as asteroids group
    Asteroid.containers = (asteroids, updatable, drawable)

    # add the asteroid field to updatable group and create its object
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # add the shots to all required groups
    Shot.containers = (shots, updatable, drawable)

    # initialize clock object
    clock = pygame.time.Clock()
    dt = 0

    while True:
        handle_close_btn()

        pygame.Surface.fill(screen, "black")
        handle_updatable(updatable, dt)
        handle_collisions(asteroids, player, shots)
        handle_drawable(drawable, screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


def main():
    pygame.init()
    print("Starting asteroids!")
    play()


if __name__ == "__main__":
    main()
