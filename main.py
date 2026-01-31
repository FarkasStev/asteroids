import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create Object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Asteroid
    Asteroid.containers = (asteroids, updatable, drawable)

    # Asteroid Field (handles spawning of asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Shot
    Shot.containers = (shots, drawable, updatable)

    # Main Game Loop
    while True:
        log_state()

        # Handle window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        screen.fill("black")
        updatable.update(dt)

        # Collision checks
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        # Draw game entities
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        # dt is the time delta (used to separate physics from frame rate)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
